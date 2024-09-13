import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Define the function for CPU utilization U(t) based on utilization percentage
def cpu_utilization(utilization_percentage):
    return utilization_percentage  # Utilization is already in percentage (20%, 50%, etc.)


# Define the ODE: dT/dt = k1 * U(t) - k2 * (T(t) - T_ambient)
def temperature_model(T, t, k1, k2, T_ambient, utilization_percentage):
    Ut = cpu_utilization(utilization_percentage)  # Get the CPU utilization
    dTdt = k1 * Ut - k2 * (T - T_ambient)  # ODE in Fahrenheit
    return dTdt


# Fixed constants (in Fahrenheit and no user input)
T0 = 77  # Initial CPU temperature in Fahrenheit
T_ambient = 77  # Ambient temperature in Fahrenheit
k1 = 0.01  # Heat generation constant (utilization to °F conversion factor)
k2 = 0.02  # Cooling constant (cooling rate in °F per second)

# Time points (from 0 to 500 seconds, with 1000 intervals)
t = np.linspace(0, 500, 1000)

# CPU utilization percentages to simulate
utilization_percentages = [20, 50, 80, 100]  # In percentages

# Plotting the results
plt.figure()

for utilization in utilization_percentages:
    # Solve the ODE for each utilization percentage
    T_solution = odeint(temperature_model, T0, t, args=(k1, k2, T_ambient, utilization))

    # Plot the result for this utilization
    plt.plot(t, T_solution, label=f'Utilization {utilization}%')

# Adding labels and title to the plot
plt.xlabel('Time (seconds)')
plt.ylabel('CPU Temperature (°F)')
plt.title('CPU Temperature Over Time for Different CPU Utilizations (Fahrenheit)')
plt.grid(True)
plt.legend()
plt.show()
