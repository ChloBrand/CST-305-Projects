
# Lorenz Attractor and Queue Analysis Programs

This repository contains two Python programs designed to explore mathematical and computational concepts:

1. **Program 1: Lorenz Attractor Visualization** - Models the Lorenz attractor and demonstrates its dynamics.
2. **Program 2: Queue Analysis in a Single-Server System** - Analyzes queue behavior and computes key performance metrics for a first-come, first-served (FCFS) single-server queue.

---

## Program 1: Lorenz Attractor Visualization

The Lorenz attractor is a system of three differential equations that models chaotic behavior. This program visualizes the Lorenz attractor's 3D path and its X, Y, and Z components based on user-defined parameters.

### Features:
- Interactive input for `σ`, `ρ`, and `β` parameters.
- Visualizes the Lorenz attractor in 3D and its individual components over time.
- Demonstrates transitions between stable, in-between, and chaotic states.

### Equations:
The Lorenz system is defined as:
```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```
Where:
- `σ`: Prandtl number (controls convection rate).
- `ρ`: Rayleigh number (drives the system).
- `β`: A constant related to the physical dimensions.

### How to Use:
1. Run the program.
2. Enter values for `ρ` corresponding to different states (stable, in-between, chaotic).
3. View the generated plots:
   - A 3D plot of the Lorenz attractor.
   - X, Y, and Z components plotted separately over time.

### Example Output:
- 3D representation of the attractor.
- Line plots showing how each variable evolves over time.

---

## Program 2: Queue Analysis in a Single-Server System

This program analyzes queue behavior in a single-server system where customers arrive and are served in a first-come, first-served (FCFS) manner. The program computes important metrics and generates insightful visualizations.

### Features:
1. **Queue Metrics:**
   - `Lq`: Time-average number in the queue.
   - `Lq^A`: Average number in the queue as seen by arriving customers.

2. **Generated Visualizations:**
   - Arrival time vs. service start time.
   - Arrival time vs. exit time.
   - Arrival time vs. time in queue.
   - Arrival time vs. number of customers in the system.
   - Arrival time vs. number of customers in the queue.

3. **Scaling Analysis:** Demonstrates the effect of scaling arrival (`λ`) and service (`μ`) rates on:
   - Utilization (`ρ`)
   - Throughput (`X`)
   - Mean number in the system (`E[N]`)
   - Mean time in the system (`E[T]`)

### How to Use:
1. Run the program.
2. View the metrics and visualizations.
3. Observe scaling effects by analyzing the plots for different scaling factors.

### Example Input Data:
| Arrival Time (min) | Service Duration (min) |
|---------------------|-------------------------|
| 1                   | 2.22                   |
| 2                   | 1.76                   |
| ...                 | ...                    |
| 15                  | 0.27                   |

### Example Output:
- Key queue metrics (`Lq`, `Lq^A`).
- Five plots illustrating queue behavior over time.
- Four plots showing the impact of scaling arrival and service rates.

---

## Setup Instructions

1. Clone the repository.
2. Ensure Python 3.7+ is installed.
3. Install dependencies using:
   ```bash
   pip install numpy pandas matplotlib
   ```
4. Run the programs:
   - **Program 1**: `python program1.py`
   - **Program 2**: `python program2.py`

---

## Dependencies:
- `numpy`: For numerical computations.
- `pandas`: For data handling in the queue analysis program.
- `matplotlib`: For generating visualizations.

---

## Authors
- **Gabriel VanderKlok**
- **Chloe Brandow**

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments
- The Lorenz attractor program is inspired by coursework on dynamical systems and chaos theory.
- The queue analysis program is based on theoretical concepts from queueing theory and single-server systems.

