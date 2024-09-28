
# Runge-Kutta VS ODEint

This project compares two numerical methods for solving ordinary differential equations (ODEs): the built-in `odeint` function from the `scipy.integrate` module and a custom implementation of the Runge-Kutta method. The solution of the ODE `dy/dx = y/(e^x-1)` is computed using both methods and the results are plotted for visual comparison.


## Purpose

The goal of this project is to demonstrate the performance and accuracy of two different numerical solvers for ODEs:
1. `odeint` — a built-in Python solver using advanced numerical methods.
2. Runge-Kutta — a custom implementation of the classical 4th-order Runge-Kutta method.

The execution time of each solver is measured using the `timeit` module for performance analysis.

## Requirements

To run this code, you need the following Python libraries:

- `numpy`
- `scipy`
- `matplotlib`
- `timeit` (built-in Python module)

## Installation

You can install the required libraries using `pip`:

```bash
pip install numpy scipy matplotlib
```

## Usage

1. Clone or download the repository.
2. Run the Python script:
3. The script will display the time taken by each solver (`odeint` and Runge-Kutta) and plot the solutions using `matplotlib`.

## Code
```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import timeit

# Define the ODE function dy/dx = y/(e^x-1)
def ode_func(y, x):
    global odeint_steps
    odeint_steps += 1  # Increment step count for odeint
    return y / (math.exp(x) - 1)

# Runge-Kutta method implementation
def runge_kutta(f, x0, y0, xf, h):
    x_values = np.arange(x0, xf + h, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0
    rk_steps = 0  # Initialize step counter for Runge-Kutta

    for i in range(1, len(x_values)):
        x = x_values[i - 1]
        y = y_values[i - 1]

        k1 = f(x, y)
        k2 = f(x + 0.5 * h, y + (0.5 * h * k1))
        k3 = f(x + 0.5 * h, y + (0.5 * h * k2))
        k4 = f(x + h, y + h * k3)

        y_values[i] = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        rk_steps += 4  # Each iteration computes 4 intermediate values (k1, k2, k3, k4)

    return x_values, y_values, rk_steps

# Function for the ODE used in Runge-Kutta
def f(x, y):
    global rk_steps
    rk_steps += 1  # Increment step count for Runge-Kutta in function evaluation
    return y / (math.exp(x) - 1)

# Initial conditions and parameters
x0 = 1
y0 = 5
h = 0.02
x_end = 10

# Global variable to keep track of steps
odeint_steps = 0
rk_steps = 0

# Generate the array of x values for odeint
x_vals_odeint = np.arange(x0, x_end + h, h)

# Measure time and steps for odeint solution
odeint_time = timeit.timeit(lambda: odeint(ode_func, y0, x_vals_odeint), number=1)
# Solve the ODE using odeint
y_vals_odeint = odeint(ode_func, y0, x_vals_odeint)

# Measure time and steps for Runge-Kutta solution
runge_kutta_time = timeit.timeit(lambda: runge_kutta(f, x0, y0, x_end, h), number=1)
# Solve the ODE using Runge-Kutta method and count steps
x_vals_rk, y_vals_rk, rk_steps = runge_kutta(f, x0, y0, x_end, h)

# Print elapsed times and computational steps
print(f"Time taken by odeint: {odeint_time:.6f} seconds")
print(f"Computational steps by odeint: {odeint_steps}")

print(f"Time taken by Runge-Kutta: {runge_kutta_time:.6f} seconds")
print(f"Computational steps by Runge-Kutta: {rk_steps}")

# Plot odeint result
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(x_vals_odeint, y_vals_odeint, label='odeint', color='blue')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solution of ODE using odeint')
plt.legend()
plt.grid(True)

# Plot Runge-Kutta result
plt.subplot(1, 3, 2)
plt.plot(x_vals_rk, y_vals_rk, label='Runge-Kutta', color='red', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solution of ODE using Runge-Kutta')
plt.legend()
plt.grid(True)

# Plot both results together for comparison
plt.subplot(1, 3, 3)
plt.plot(x_vals_odeint, y_vals_odeint, label='odeint', color='blue')
plt.plot(x_vals_rk, y_vals_rk, label='Runge-Kutta', color='red', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Comparison of odeint and Runge-Kutta')
plt.legend()
plt.grid(True)

# Display all plots
plt.tight_layout()
plt.show()

```

## Results

The script will output the time taken by each solver to solve the ODE:

```
Time taken by odeint: X.XXXXXX seconds
Time taken by Runge-Kutta: X.XXXXXX seconds
```

The generated plots will include:
1. **Solution of ODE using `odeint`** — The solution using the built-in `odeint` function.
2. **Solution of ODE using Runge-Kutta** — The solution using the custom Runge-Kutta implementation.
3. **Comparison of `odeint` and Runge-Kutta** — A side-by-side comparison of the results from both methods.

### Visual Representation:

- The first plot shows the solution obtained using `odeint`.
- The second plot shows the solution obtained using the Runge-Kutta method.
- The third plot overlays both solutions for comparison.

## License

This project is open-source and available under the MIT License.
