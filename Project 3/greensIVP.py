# Chloe Brandow and Gabriel VanderKlok
# CST - 305
# Professor Richardo Citro
# September 20, 2024
# Project 3 - Green's Function and ODE with IVP

import numpy as np
import matplotlib.pyplot as plt

# Time range
t = np.linspace(0, 25, 100)

# First Equation: General solution y(t) = -4 * cos(t) + 4
y_1_general = -4 * np.cos(t) + 4

# First Equation: Homogeneous solution y_h(t) = -4 * cos(t)
y_1_homogeneous = -4 * np.cos(t)

# Second Equation: General solution y(t) = (1/8) * cos(2t) + (1/4) * t**2 - (1/8)
y_2_general = (1/8) * np.cos(2 * t) + (1/4) * t**2 - (1/8)

# Second Equation: Homogeneous solution y_h(t) = (1/8) * cos(2t)
y_2_homogeneous = (1/8) * np.cos(2 * t)

# Plotting the homogeneous solution for the first equation
plt.figure(figsize=(10, 5))
plt.plot(t, y_1_homogeneous, 'r--', label="Homogeneous Solution: y_h(t) = -4 cos(t)")
plt.title("First Equation: Homogeneous Solution")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.xlim(0, 10)
plt.ylim(-7, 7)
plt.show()

# Plotting the general solution for the first equation
plt.figure(figsize=(10, 5))
plt.plot(t, y_1_general, 'b-', label="General Solution: y(t) = -4 cos(t) + 4")
plt.title("First Equation: General Solution")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.xlim(0, 10)
plt.ylim(-5, 9)
plt.show()

# Plotting the homogeneous solution for the second equation
plt.figure(figsize=(10, 5))
plt.plot(t, y_2_homogeneous, 'r--', label="Homogeneous Solution: y_h(t) = (1/8) cos(2t)")
plt.title("Second Equation: Homogeneous Solution")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.xlim(0, 10)
plt.ylim(-1, 1)
plt.show()

# Plotting the general solution for the second equation
plt.figure(figsize=(10, 5))
plt.plot(t, y_2_general, 'g-', label="General Solution: y(t) = (1/8) cos(2t) + (1/4) t^2 - (1/8)")
plt.title("Second Equation: General Solution")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.xlim(0, 25)
plt.ylim(-5, 100)
plt.show()
