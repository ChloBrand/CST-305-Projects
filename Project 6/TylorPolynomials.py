# Chloe Brandow and Gabriel VanderKlok
# CST - 305
# Professor Richardo Citro
# November 24, 2024
# Project 6 – Numeric Computations with Taylor Polynomials

import numpy as np
import matplotlib.pyplot as plt


# --- Part 1 (a): Taylor Series Expansion for y'' - 2xy' + x^2y = 0 ---
def taylor_series_part_a(x):
   """
   Calculate the Taylor series approximation for the solution of the equation:
   y'' - 2xy' + x^2y = 0 with initial conditions y(0) = 1 and y'(0) = -1.
   The Taylor expansion is up to the 4th order.
   """
   # Initial conditions and coefficients of the Taylor expansion
   y = 1  # y(0)
   y_prime = -1  # y'(0)
   y_double_prime = 0  # y''(0)
   y_triple_prime = -2  # y'''(0)
   y_quad_prime = -2  # y''''(0)


   # Compute the Taylor series expansion
   y_approx = (
           y +
           y_prime * x +
           (y_double_prime * (x ** 2)) / 2 +
           (y_triple_prime * (x ** 3)) / 6 +
           (y_quad_prime * (x ** 4)) / 24
   )
   return y_approx

# Generate x values for plotting and evaluate the Taylor series
x_values_a = np.linspace(0, 4, 100)  # Values of x from 0 to 4
y_values_a = [taylor_series_part_a(x) for x in x_values_a]


# Calculate the Taylor series value at x = 3.5
y_at_3_5_a = taylor_series_part_a(3.5)
print(f"Part (a): y(3.5) ≈ {y_at_3_5_a}")


# Plot the Taylor series result
plt.figure(figsize=(10, 6))
plt.plot(x_values_a, y_values_a, label=r"$f(x) = 1 - x - \frac{x^3}{3} - \frac{x^4}{12}$", color="blue")
plt.scatter(3.5, y_at_3_5_a, color="red", label=f"y(3.5) ≈ {y_at_3_5_a:.2f}")  # Mark y(3.5)
plt.title("Part (a): Taylor Series Expansion for y'' - 2xy' + x^2y = 0")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add horizontal axis
plt.legend()
plt.grid()
plt.show()



# Part 1 (b): Computes and plots the second-order Taylor polynomial for the solution of the differential equation
# y'' - (x - 2)y' + 2y = 0 with initial conditions y(3) = 6 and y'(3) = 1. The Taylor polynomial is centered at x = 3.

def taylor_polynomial_part_b(x, x0=3, y0=6, y1=1, y2=-11):
   """
   Calculate the second-order Taylor polynomial for the solution of the equation:
   y'' - (x - 2)y' + 2y = 0 with initial conditions y(3) = 6 and y'(3) = 1.
   """
   # Use the second-order Taylor polynomial formula
   return y0 + y1 * (x - x0) + (y2 / 2) * (x - x0) ** 2

# Generate x values for plotting and evaluate the second-order Taylor polynomial
x_values_b = np.linspace(2.5, 3.5, 100)  # Values of x around x0 = 3
y_values_b = [taylor_polynomial_part_b(x) for x in x_values_b]


# Plot the second-order Taylor polynomial result
plt.figure(figsize=(8, 5))
plt.plot(x_values_b, y_values_b, label=r"$f(x) = 6 + (x-3) - \frac{11}{2}(x-3)^2$", color="blue")
plt.axvline(3, color='red', linestyle='--', label="Expansion Point (x=3)")  # Mark expansion point
plt.title("Part (b): Second-Order Taylor Polynomial for y'' - (x - 2)y' + 2y = 0")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.grid()
plt.show()


# Part 2
# assign constant value for a0 and a1

a0 = 1
a1 = 1

# General Solution define
def general_solution(x):
    y = a0 * (1 + (-1 / 8 * (x ** 2)) + (1 / 128 * (x ** 4)) + (-13 / 15360 * (x ** 6)) + (403 / 3440640 * (x ** 8)) + (
                -7657 / 412876800 * (x ** 10))) + a1 * (
                    x + (-1 / 24 * (x ** 3)) + (7 / 1920 * (x ** 5)) + (-7 / 15360 * (x ** 7)) + (
                        301 / 4423680 * (x ** 9)))

    return y

# generate x values with higher resolution
x_val = np.linspace(0, 9, 1000)
# generate corresponding y values
y_val = general_solution(x_val)

# plot the graph
plt.title('Part 2: Power Series Solution with n <= 8')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x_val, y_val)

# draw the graph
plt.show()
