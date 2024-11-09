# Lorenz Attractor Modeling

## Authors
Gabriel VanderKlok and Chloe Brandow

## Description
This project uses Numpy and Matplotlib to model the Lorenz attractor as a representation of organized criticality in a file system. It visualizes its 3D path over time along with separate X, Y, and Z component plots based on user-provided parameters.

## Code Overview

The following code defines the Lorenz attractor function and allows the user to input different values of the parameter `r`, which represents the system's behavior in three different states: stable, in-between, and chaotic. The model calculates the Lorenz attractor's trajectory and generates corresponding visualizations.

```python
import matplotlib.pyplot as plt
import numpy as np

def Lorenz(xyz, s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])
```

### Key Variables and Parameters
- **xyz**: An array representing the current state of the system in 3D space, where:
  - `x` represents one dimension of the system, which can be interpreted as a varying file size.
  - `y` represents a second dimension, also indicative of a different aspect of the file system.
  - `z` represents a third dimension, contributing to the overall state of the system.
  
- **s (sigma)**: A parameter that represents the Prandtl number, controlling the rate of change of `x` relative to `y`. The default value is `10`.

- **r (rho)**: The Rayleigh number, which determines the behavior of the system:
  - **Stable State**: A lower `r` value results in stable behavior.
  - **In-between State**: A medium `r` value shows transitional behavior.
  - **Chaotic State**: A high `r` value leads to chaotic dynamics.

- **b (beta)**: A parameter related to the physical properties of the system, set to `2.667` by default. It influences the rate of change of `z`.

### User Input
The program prompts the user to enter values for `r` corresponding to the states of the system:
```python
r_values = []
states = ["stable", "in-between", "chaotic"]
for state in states:
    r = float(input(f"Enter the r value for the {state} state: "))
    r_values.append(r)
```

### Simulation Parameters
- **dt**: The time increment for each step of the simulation, set to `0.01`.
- **num_steps**: The total number of time steps for the simulation, set to `10000`.


### Initial Conditions
- **xyzs[0]**: The initial conditions for the system, where:
  - `x` starts at `11.8 KB`, representing the initial file size in the first dimension (rough estimate for an average JPG image).
  - `y` starts at `4.4 KB`, representing the initial file size in the second dimension (rough estimate for an average PNG image).
  - `z` starts at `2.4 KB`, representing the initial file size in the third dimension (rough estimate for an average GIF image).

### Plotting Results
The code generates three types of plots:
1. **3D Attractor Plot**: Visualizes the path of the Lorenz attractor in 3D space.
2. **X Component Plot**: Shows the evolution of the `x` coordinate over time.
3. **Y Component Plot**: Displays the evolution of the `y` coordinate over time.
4. **Z Component Plot**: Illustrates the evolution of the `z` coordinate over time.

### Running the Code
To run the code, ensure you have the required libraries installed:
```bash
pip install matplotlib numpy
```
Then execute the script in a Python environment.

## Conclusion
This model provides a visual representation of chaotic systems using the Lorenz attractor, allowing for a better understanding of dynamic behavior in complex systems like file fragmentation and organization.
