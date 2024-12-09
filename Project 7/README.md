
# Lorenz Attractor and Queue Analysis Programs

This repository contains two Python programs developed for computational and analytical tasks, focusing on dynamical systems and queue theory. The projects are designed to enhance understanding of the Lorenz attractor and queue behavior in a single-server system.

## Program 1: Lorenz Attractor Visualization

This program models the Lorenz attractor using three ordinary differential equations (ODEs). It provides interactive visualization of the attractor's 3D path and its X, Y, and Z components for various user-defined parameter values.

### Features:
- Allows user input for the `σ`, `ρ`, and `β` parameters.
- Visualizes the Lorenz attractor's 3D path and separate component plots.
- Demonstrates the effects of parameter changes on the attractor's dynamics.

### Equations:
The Lorenz attractor is defined by the following ODEs:
```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```a
Where:
- `σ` represents the Prandtl number.
- `ρ` represents the Rayleigh number.
- `β` is a geometric factor.

### Usage:
1. Run the program.
2. Input the `ρ` values for "stable," "in-between," and "chaotic" states as prompted.
3. View the generated 3D plot and the X, Y, and Z component plots.

### Dependencies:
- `numpy`
- `matplotlib`

---

## Program 2: Queue Analysis in a Single-Server System

This program analyzes a first-come, first-served (FCFS) single-server queue using arrival times and service durations provided in a table. It computes key metrics and visualizes queue behavior over time.

### Features:
1. Computes:
   - `Lq`: Time-average number in the queue.
   - `Lq^A`: Average number in the queue as seen by arriving customers.
2. Generates five visualizations:
   - Arrival time vs. service start time.
   - Arrival time vs. exit time.
   - Arrival time vs. time in queue.
   - Arrival time vs. number of customers in the system.
   - Arrival time vs. number of customers in the queue.
3. Analyzes scaling effects of arrival and service rates (`λ` and `μ`) on key performance metrics in an M/M/1 system.

### Usage:
1. Run the program.
2. View the computed metrics and generated plots for queue analysis.
3. Observe the scaling effects of `λ` and `μ` on:
   - Utilization (`ρ`)
   - Throughput (`X`)
   - Mean number in the system (`E[N]`)
   - Mean time in the system (`E[T]`)

### Dependencies:
- `numpy`
- `pandas`
- `matplotlib`

### Example Input Data:
| Arrival Time (min) | Service Duration (min) |
|---------------------|-------------------------|
| 1                   | 2.22                   |
| 2                   | 1.76                   |
| ...                 | ...                    |
| 15                  | 0.27                   |

---

## Setup Instructions

1. Clone the repository.
2. Ensure Python 3.7+ is installed.
3. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib
   ```
4. Run the desired program using:
   ```bash
   python program1.py  # For Lorenz attractor visualization
   python program2.py  # For queue analysis
   ```

---

## Outputs

### Program 1:
- 3D plot of the Lorenz attractor.
- Line plots of the X, Y, and Z components.

### Program 2:
- Queue metrics (`Lq`, `Lq^A`).
- Five interactive plots for queue behavior.
- Four performance metric visualizations for scaled arrival and service rates.

---

## Authors
- **Gabriel VanderKlok**
- **Chloe Brandow**

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments
- Inspired by coursework on dynamical systems and queueing theory.
- Special thanks to professor Citro for guidance on computational modeling.
