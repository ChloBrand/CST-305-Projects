# Numerical Integration
# Created by Chloe Brandow and Gabriel VanderKlok
# Date: 12.13.24
#
# This program approximates definite integrals using Riemann sums (Left, Midpoint, Right).
# It utilizes Python's numpy and matplotlib libraries for numerical computation and visualization.
# The approach involves defining continuous functions and calculating the Riemann sums
# over specified intervals with user-defined subintervals. Both graphs and numerical results are provided.

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi
from scipy.integrate import quad  # Import for calculating the actual integral value

# Function declarations
partA = lambda x: np.sin(x) + 1
partB = lambda x: (3 * x) + (2 * (x ** 2))
partC_1 = lambda x: np.log(x)
partC_2 = lambda x: (x ** 2) - (x ** 3)
part2 = lambda x: -0.0024 * x ** 4 + 0.1194 * x ** 3 - 1.3886 * x ** 2 - 1.4721 * x + 77.72

# Graph steps
steps = 100


# Function to calculate and graph left, mid, and right sums given a function and its parameters
def graphRiemannApproximation(f, lower, upper, n, title, units=""):
    # Get x at equally spaced n+1 points between lower and upper
    x1 = np.linspace(lower, upper, n + 1)
    x2 = np.linspace(lower, upper, steps * n + 1)

    # Calculate y values
    y1 = f(x1)
    y2 = f(x2)

    plt.figure(figsize=(15, 5))

    # Left subplot
    plt.subplot(1, 3, 1)
    plt.plot(x2, y2, 'r')
    x_left = x1[:-1]
    y_left = y1[:-1]
    plt.bar(x_left, y_left, width=(upper - lower) / n, align='edge', color='blue', alpha=0.4)
    plt.title(f'Left (n = {n})')
    if title == "Part 2":
        plt.xlabel("Minutes")
        plt.ylabel(f"Download Rate ({units})")

    # Midpoint subplot
    plt.subplot(1, 3, 2)
    plt.plot(x2, y2, 'y')
    x_mid = (x1[:-1] + x1[1:]) / 2
    y_mid = f(x_mid)
    plt.bar(x_mid, y_mid, width=(upper - lower) / n, align='center', color='purple', alpha=0.4)
    plt.title(f'Midpoint (n = {n})')
    if title == "Part 2":
        plt.xlabel("Minutes")
        plt.ylabel(f"Download Rate ({units})")

    # Right subplot
    plt.subplot(1, 3, 3)
    plt.plot(x2, y2, 'g')
    x_right = x1[1:]
    y_right = y1[1:]
    plt.bar(x_right, y_right, width=(upper - lower) / n, align='edge', color='green', alpha=0.4)
    plt.title(f'Right (n = {n})')
    if title == "Part 2":
        plt.xlabel("Minutes")
        plt.ylabel(f"Download Rate ({units})")

    # Part 2 graph
    if title == "Part 2":
        plt.suptitle(f"Part 2: Total Data Transferred\nRiemann Sum Approximation", fontsize=14)
    else:
        plt.suptitle(f"Riemann Sum Approximation for {title}")

    plt.tight_layout()
    plt.show()


# Calculate and print left, mid, and right sums, and the actual integral value
def RiemannApproximation(f, lower, upper, n, part):
    print(f"\nPart {part}")
    step = (upper - lower) / n
    x_left = np.linspace(lower, upper - step, n)
    x_mid = (x_left + step / 2)
    x_right = np.linspace(lower + step, upper, n)

    # Riemann Sums
    left_sum = np.sum(f(x_left) * step)
    mid_sum = np.sum(f(x_mid) * step)
    right_sum = np.sum(f(x_right) * step)

    # Actual Integral
    actual_sum, _ = quad(f, lower, upper)

    # Print results
    print(f"Left Sum: {left_sum:.2f}")
    print(f"Midpoint Sum: {mid_sum:.2f}")
    print(f"Right Sum: {right_sum:.2f}")
    print(f"Actual Sum: {actual_sum:.2f}")


# Call the function for all parts
graphRiemannApproximation(partA, -pi, pi, 4, "Part A")
graphRiemannApproximation(partB, 0, 1, 10, "Part B")
graphRiemannApproximation(partC_1, 1, np.e, 1000, "Part C_1")
graphRiemannApproximation(partC_2, -1, 0, 30, "Part C_2")
graphRiemannApproximation(part2, 1, 30, 50, "Part 2", units="Mbps")

RiemannApproximation(partA, -pi, pi, 4, "A")
RiemannApproximation(partB, 0, 1, 30, "B")
RiemannApproximation(partC_1, 1, np.e, 30, "C_1")
RiemannApproximation(partC_2, -1, 0, 30, "C_2")
RiemannApproximation(part2, 0, 30, 50, "2")
