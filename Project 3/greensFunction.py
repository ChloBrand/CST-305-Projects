# Chloe Brandow and Gabriel VanderKlok
# CST - 305
# Professor Richardo Citro
# September 20, 2024
# Project 3 - Green's Function and ODE with IVP

# Import Packages to Use
import numpy as np
import matplotlib.pyplot as plt
import math

# First Equation
def homo_two(x):                            # Define the homogeneous solution
    return -4 * math.cos(x)

x = np.linspace(0, 1, 100)   # Create a space for x axis
h_2 = [] # Apply solution value to function
for i in range(100):
    h_2.append(homo_two(i))

# Graphing
plt.figure(3)
plt.plot(x, h_2)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph of y(x) = Homogeneous Second Equation Solution")
plt.grid()


# Define the Green's solution
def green_two(x):
    return (-4 * math.cos(x)) + 4

x = np.linspace(0, 1, 100)
g_2 = []
for i in range(100):
    g_2.append(green_two(i))

# Graphing
plt.figure(4)
plt.plot(x, g_2)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph of y(x) = Green's Second Equation Solution")
plt.grid()
plt.show()


# -------------------------------------------------------------------------------- #
# Second Equation
def homo_one(x):                        # Define the homogeneous solution
    return (3/4)-(3/4)*math.e**(-2*x)

# Assign the space for x axis
x = np.linspace(0, 10, 1000)
y = homo_one(x)

# Graph process
plt.figure(1)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y(x) = Homogeneous First Equation Solution')
plt.grid()


# Define Green's solution for equation one
def green_one(x):
    return ((3/4)-(3/4)*math.e**(-2*x)+(1/2)*x**2 - (3/2)*x)

x = np.linspace(0, 10, 1000)
y = green_one(x)

plt.figure(2)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Graph of y(x) = Green's First Equation Solution")
plt.grid()

