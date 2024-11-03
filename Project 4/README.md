
# Degradation of Data Integrity - Project 4

**Authors**: Chloe Brandow and Gabriel VanderKlok  
**Course**: CST - 305  
**Instructor**: Professor Richardo Citro  
**Date**: November 3, 2024  

---

## Project Overview

This project involves analyzing the degradation of data integrity using a matrix method to solve ordinary differential equations (ODEs). The objective is to derive and visualize two solutions that describe the behavior of data degradation over time.

---

## Code Explanation

```python
import numpy as np
import matplotlib.pyplot as plt

# Part 2 solution 1
def x_one(t):
    return np.exp(-0.05 * t)  # Returns solution found from e^At

# Part 2 solution 2
def x_two(t):
    return (-1 * np.exp(-0.05 * t))

# Visualization
t_space = np.linspace(-100, 100, 200)  # Testing 0 to 100 x points
x1space = []
x2space = []
for i in t_space:
    x1space.append(x_one(i))  # Fill first solution space for solution 1
    x2space.append(x_two(i))  # Fill second solution space for solution 2

# Drawing the chart and some labels
plt.title("Degradation of Data Integrity - ODE Solutions by Matrix Method")
plt.xlabel("t")  # Name for x-axis
plt.ylabel("x")  # Name for y-axis

plt.plot(t_space, x1space, label='e^-0.05t')  # Plot the point
plt.plot(t_space, x2space, label='-e^-0.05t')  # Plot the point

plt.ylim(-50, 50)  # y-window for -50 to 50
plt.xlim(-100, 100)  # x-window for -100 to 100
plt.grid()
plt.legend()
plt.show()
```

---

## Description

- **x_one(t)**: Computes the first solution using the exponential decay model.
- **x_two(t)**: Computes the second solution, which is the negative of the first.
- **t_space**: Defines a range from -100 to 100 for plotting the solutions.
- The code generates and visualizes two ODE solutions that illustrate data degradation over time, using a line plot for better understanding.

---

## Visualization

The graph titled *"Degradation of Data Integrity - ODE Solutions by Matrix Method"* shows two curves:
- `e^-0.05t`: Represents the gradual decrease in data integrity over time.
- `-e^-0.05t`: Represents the mirrored decay effect in the negative direction.

The plot is configured with labeled axes, a legend, and grid lines for clarity.

---

## Conclusion

This project demonstrates the degradation of data integrity using mathematical modeling and visualization. The exponential decay functions effectively illustrate how data integrity diminishes over time.
