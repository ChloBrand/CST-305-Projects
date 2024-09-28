# Created by Chloe Brandow and Gabriel Vander Klok
# Packages used include numpy, matplotlib, math, timeit, and scipy
# The implementation uses the built-in odeint function from scipy and a custom
# 4th-order Runge-Kutta method to solve an ordinary differential equation for
# comparison. The timeit module is used to measure and compare the performance
# of both methods, and the results are plotted using matplotlib for visual analysis.

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
