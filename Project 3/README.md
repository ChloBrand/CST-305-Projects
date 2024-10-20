# Project 3 - Green's Function and ODE with IVP

**Course**: CST - 305  
**Professor**: Richardo Citro  
**Project Date**: September 20, 2024  
**Team Members**: Chloe Brandow, Gabriel VanderKlok  

## Project Overview

This project demonstrates the application of Green's function and solving ordinary differential equations (ODEs) with initial value problems (IVP). The solutions include both the homogeneous and general solutions for two different equations.

The code is implemented in Python using `NumPy` for numerical calculations and `Matplotlib` for visualizing the solutions.

## Equations Solved

### First Equation
The first equation solved is:

```
y'' + y = 4
```

- **Homogeneous Solution**:  
  ```
  y_h(t) = -4 cos(t)
  ```

- **General Solution**:  
  ```
  y(t) = -4 cos(t) + 4
  ```

### Second Equation
The second equation solved is:

```
y'' + 4y = t^2
```

- **Homogeneous Solution**:  
  ```
  y_h(t) = (1/8) cos(2t)
  ```

- **General Solution**:  
  ```
  y(t) = (1/8) cos(2t) + (1/4) t^2 - (1/8)
  ```

## Visualization

The project visualizes both the **homogeneous** and **general solutions** for each of the equations using Matplotlib. The solutions are plotted on separate graphs for clarity.

### First Equation

- **Homogeneous Solution**: The solution oscillates as a cosine function with an amplitude of 4.
- **General Solution**: The solution is a cosine function shifted upwards by 4 units.

### Second Equation

- **Homogeneous Solution**: The solution oscillates with a smaller amplitude, corresponding to the cosine term.
- **General Solution**: This solution is a combination of a parabolic term and a cosine term.

## Code Files

### `main.py`

This file contains the Python code for the project. The equations are solved and plotted using `NumPy` for the mathematical functions and `Matplotlib` for the visualizations.

The following plots are generated:
1. **Homogeneous Solution for the First Equation**: A cosine oscillation with bounds between -7 and 7.
2. **General Solution for the First Equation**: A cosine oscillation with a vertical shift of 4, plotted between -5 and 9.
3. **Homogeneous Solution for the Second Equation**: A small amplitude cosine oscillation with bounds between -1 and 1.
4. **General Solution for the Second Equation**: A combination of parabolic and oscillatory behavior, plotted with bounds from -5 to 100.

### Instructions for Running the Code

1. **Install Dependencies**:  
   Ensure you have Python 3.x installed on your system. Install the required packages using `pip`:

   ```bash
   pip install numpy matplotlib
   ```

2. **Run the Python Script**:  
   Run the `main.py` script to generate the plots:

   ```bash
   python main.py
   ```

3. **View the Plots**:  
   After running the script, four separate plots will be displayed:
   - Homogeneous solution for the first equation.
   - General solution for the first equation.
   - Homogeneous solution for the second equation.
   - General solution for the second equation.

## Project Structure

```
Project/
│
├── main.py         # Python script that solves and visualizes the ODEs
├── README.md       # Project documentation
└── requirements.txt  # Optional: List of dependencies (NumPy, Matplotlib)
```

### Example Output

The program will display four graphs as output:

1. **Homogeneous Solution - First Equation**  
   A red dashed plot showing the cosine-based homogeneous solution.

2. **General Solution - First Equation**  
   A blue plot showing the general solution that combines a cosine and constant term.

3. **Homogeneous Solution - Second Equation**  
   A red dashed plot showing the small amplitude oscillations from the homogeneous solution.

4. **General Solution - Second Equation**  
   A green plot showing a combination of parabolic growth and oscillation.

## License

This project is released under the MIT License.

## Acknowledgments

We would like to thank Professor Richardo Citro for his guidance and support throughout this project.
