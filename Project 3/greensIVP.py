# Chloe Brandow and Gabriel VanderKlok
# CST - 305
# Professor Richardo Citro
# September 20, 2024
# Project 3 - Green's Function and ODE with IVP

import numpy as np
import matplotlib.pyplot as plt

# Time range
t = np.linspace(0, 10, 100)

# First Equation: General solution y(t) = -4 * cos(t) + 4
y_1_general = -4 * np.cos(t) + 4

# First Equation: Homogeneous solution y_h(t) = -4 * cos(t)
y_1_homogeneous = -4 * np.cos(t)

# Second Equation: General solution y(t) = (1/8) * cos(2t) + (1/4) * t^2 - (1/8)
y_2_general = (1/8) * np.cos(2 * t) + (1/4) * t**2 - (1/8)

# Second Equation: Homogeneous solution y_h(t) = (1/8) * cos(2t)
y_2_homogeneous = (1/8) * np.cos(2 * t)

# Plotting the solutions
plt.figure(figsize=(10, 8))

# Plot first equation solutions
plt.subplot(2, 1, 1)
plt.plot(t, y_1_general, 'b-', label="General Solution: y(t) = -4 cos(t) + 4")
plt.plot(t, y_1_homogeneous, 'r--', label="Homogeneous Solution: y_h(t) = -4 cos(t)")
plt.title("First Equation: General and Homogeneous Solutions")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

# Plot second equation solutions
plt.subplot(2, 1, 2)
plt.plot(t, y_2_general, 'g-', label="General Solution: y(t) = (1/8) cos(2t) + (1/4) t^2 - (1/8)")
plt.plot(t, y_2_homogeneous, 'r--', label="Homogeneous Solution: y_h(t) = (1/8) cos(2t)")
plt.title("Second Equation: General and Homogeneous Solutions")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
