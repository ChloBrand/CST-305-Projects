
# ODE Solver Comparison using Python

This project compares two numerical methods for solving ordinary differential equations (ODEs): the built-in `odeint` function from the `scipy.integrate` module and a custom implementation of the Runge-Kutta method. The solution of the ODE `dy/dx = y/(e^x-1)` is computed using both methods and the results are plotted for visual comparison.

## Table of Contents
- [Purpose](#purpose)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

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

```bash
python ode_solver_comparison.py
```

3. The script will display the time taken by each solver (`odeint` and Runge-Kutta) and plot the solutions using `matplotlib`.

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
