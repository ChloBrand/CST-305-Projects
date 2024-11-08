#Gabriel VanderKlok and Chloe Brandow
#This code uses Numpy and Matplotlib to model the Lorenz attractor as a
# representation of organized criticality in a file system, visualizing its 3D path over time
# along with separate X, Y, and Z component plots based on user-provided parameters.

import matplotlib.pyplot as plt
import numpy as np

"""
Define the Lorenz attractor function.
x, y, z are points in space that represent varying file sizes,
and s, r, b are parameters defining the Lorenz attractor.
Returns:
   x_dot, y_dot, z_dot: values of the Lorenz attractor's partial
   derivatives at the point x, y, z.
"""

def Lorenz(xyz, s=10, r=28, b=2.667):
   x, y, z = xyz
   x_dot = s * (y - x)
   y_dot = r * x - y - x * z
   z_dot = x * y - b * z
   return np.array([x_dot, y_dot, z_dot])


# Ask the user for the value of r
r_values = []
states = ["stable", "in-between", "chaotic"]
for state in states:
   r = float(input(f"Enter the r value for the {state} state: "))
   r_values.append(r)


# Setting the number of steps and increment of t
dt = 0.01
num_steps = 10000


# Initialize array to store (x, y, z) values
xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (11.8, 4.4, 2.4)  # Set initial values of the file sizes


for idx, r in enumerate(r_values):
   for i in range(num_steps):
       xyzs[i + 1] = xyzs[i] + Lorenz(xyzs[i], r=r) * dt


   # Plot the 3D attractor
   fig = plt.figure()
   ax = fig.add_subplot(projection='3d')
   ax.plot(*xyzs.T, lw=0.5)
   ax.set_xlabel("X Axis")
   ax.set_ylabel("Y Axis")
   ax.set_zlabel("Z Axis")
   ax.set_title(f"Lorenz Attractor (r = {r})")


   # Plot the x component
   fig, ax = plt.subplots()
   ax.plot(xyzs[:, 0], lw=0.5)
   ax.set_xlabel("Time Step")
   ax.set_ylabel("X Coordinate")
   ax.set_title(f"Lorenz Attractor: X Component (r = {r})")


   # Plot the y component
   fig, ax = plt.subplots()
   ax.plot(xyzs[:, 1], lw=0.5)
   ax.set_xlabel("Time Step")
   ax.set_ylabel("Y Coordinate")
   ax.set_title(f"Lorenz Attractor: Y Component (r = {r})")


   # Plot the z component
   fig, ax = plt.subplots()
   ax.plot(xyzs[:, 2], lw=0.5)
   ax.set_xlabel("Time Step")
   ax.set_ylabel("Z Coordinate")
   ax.set_title(f"Lorenz Attractor: Z Component (r = {r})")


plt.show()
