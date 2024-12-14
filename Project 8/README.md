
# Numerical Integration Project

## Overview

This project demonstrates how to approximate definite integrals using Riemann sums (Left, Midpoint, and Right methods) alongside calculating the actual integral value. The program employs Python's `numpy`, `matplotlib`, and `scipy` libraries for numerical computations and graphical visualization.

## Features

1. **Integration Methods**:
   - Left Riemann Sum
   - Midpoint Riemann Sum
   - Right Riemann Sum
   - Exact value using numerical integration (`quad` function from `scipy.integrate`)

2. **Graphical Visualizations**:
   - Displays bar plots for Left, Midpoint, and Right Riemann sums.
   - Customizable labels for Part 2 (e.g., x-axis as "Minutes" and y-axis as "Mbps").

3. **Functions Covered**:
   - `sin(x) + 1`
   - Polynomials
   - Logarithmic functions
   - Real-world scenarios like download rates over time

## Code Highlights

### Libraries Used
- **`numpy`**: For numerical calculations and array handling.
- **`matplotlib`**: For plotting graphs of Riemann sums.
- **`scipy.integrate`**: For calculating the actual integral value.

### Key Functions
1. **`graphRiemannApproximation`**:
   - Plots the Left, Midpoint, and Right Riemann sums.
   - Adds appropriate labels for axes and titles.
   - Specifically customized for Part 2 to show "Minutes" and "Mbps".

2. **`RiemannApproximation`**:
   - Computes the Left, Midpoint, and Right Riemann sums.
   - Calculates the actual integral value using the `quad` function.

## Example Usage

### Sample Output

#### Numerical Results:
```
Part 2
Left Sum: 1238.56
Midpoint Sum: 1240.67
Right Sum: 1242.78
Actual Sum: 1241.33
```

#### Graphs:
- Displays visual approximations of the integrals for various functions.
- For Part 2, axes are labeled "Minutes" and "Mbps".

## How to Run

1. Install the required libraries:
   ```bash
   pip install numpy matplotlib scipy
   ```

2. Run the Python script:
   ```bash
   python numerical_integration.py
   ```

3. View the numerical results in the console and graphical plots displayed for each function.

## File Structure
- `numerical_integration.py`: Main Python script containing all functions and logic.
- **Generated Graphs**: Displays plots for Riemann sum approximations.

## Authors
- Chloe Brandow
- Gabriel VanderKlok

## Date
December 13, 2024
