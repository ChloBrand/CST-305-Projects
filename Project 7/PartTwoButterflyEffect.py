import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Input data
data = {
    "Arrival Time": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Service Duration": [2.22, 1.76, 2.13, 0.14, 0.76, 0.7, 0.47, 0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Compute service start and exit times
service_start_times = []
exit_times = []
server_free_time = 0

for i, row in df.iterrows():
    arrival_time = row["Arrival Time"]
    service_duration = row["Service Duration"]

    service_start_time = max(arrival_time, server_free_time)
    service_start_times.append(service_start_time)

    exit_time = service_start_time + service_duration
    exit_times.append(exit_time)

    server_free_time = exit_time

df["Service Start Time"] = service_start_times
df["Exit Time"] = exit_times

# Compute time in queue
df["Time in Queue"] = df["Service Start Time"] - df["Arrival Time"]

# Compute L_q (time average number in queue)
time_horizon = 15.27
time_intervals = sorted(set(df["Arrival Time"].tolist() + df["Exit Time"].tolist()))
queue_lengths = []

for t1, t2 in zip(time_intervals[:-1], time_intervals[1:]):
    time_in_interval = t2 - t1
    num_in_queue = sum((df["Arrival Time"] <= t1) & (df["Exit Time"] > t1))
    queue_lengths.append(num_in_queue * time_in_interval)

L_q = sum(queue_lengths) / time_horizon

# Compute L_q^(A) (average number in queue as seen by arriving customers)
L_q_A = df["Time in Queue"].mean()

# Print results
L_q, L_q_A

# Plot 1: Customer arrival time vs. service start time
plt.figure()
plt.plot(df["Arrival Time"], df["Service Start Time"], marker='o', label='Service Start Time')
plt.xlabel("Arrival Time (min)")
plt.ylabel("Service Start Time (min)")
plt.title("Customer Arrival Time vs. Service Start Time")
plt.grid()
plt.legend()
plt.show()

# Plot 2: Customer arrival time vs. exit time
plt.figure()
plt.plot(df["Arrival Time"], df["Exit Time"], marker='o', label='Exit Time')
plt.xlabel("Arrival Time (min)")
plt.ylabel("Exit Time (min)")
plt.title("Customer Arrival Time vs. Exit Time")
plt.grid()
plt.legend()
plt.show()

# Plot 3: Customer arrival time vs. time in queue
plt.figure()
plt.plot(df["Arrival Time"], df["Time in Queue"], marker='o', label='Time in Queue')
plt.xlabel("Arrival Time (min)")
plt.ylabel("Time in Queue (min)")
plt.title("Customer Arrival Time vs. Time in Queue")
plt.grid()
plt.legend()
plt.show()

# Plot 4: Customer arrival time vs. number of customers in the system at that time
num_in_system = [
    sum((df["Arrival Time"] <= t) & (df["Exit Time"] > t))
    for t in df["Arrival Time"]
]
plt.figure()
plt.plot(df["Arrival Time"], num_in_system, marker='o', label='Number in System')
plt.xlabel("Arrival Time (min)")
plt.ylabel("Number in System")
plt.title("Customer Arrival Time vs. Number of Customers in System")
plt.grid()
plt.legend()
plt.show()

# Plot 5: Customer arrival time vs. number of customers in queue at that time
num_in_queue = [
    sum((df["Arrival Time"] < t) & (df["Service Start Time"] > t))
    for t in df["Arrival Time"]
]
plt.figure()
plt.plot(df["Arrival Time"], num_in_queue, marker='o', label='Number in Queue')
plt.xlabel("Arrival Time (min)")
plt.ylabel("Number in Queue")
plt.title("Customer Arrival Time vs. Number of Customers in Queue")
plt.grid()
plt.legend()
plt.show()


# Part 2 Section 3 Code:
# Define original parameters
lambda_original = 0.5  # Original arrival rate
mu_original = 1.0      # Original service rate
k_values = np.linspace(1, 5, 100)  # Scaling factor k (range from 1 to 5)


# Scale the arrival and service rates by factor k
lambda_scaled = lambda_original * k_values
mu_scaled = mu_original * k_values


# a. Utilization (ρ)
rho_original = lambda_original / mu_original
rho_scaled = lambda_scaled / mu_scaled  # Utilization remains constant


# b. Throughput (X)
throughput_scaled = lambda_scaled  # Throughput equals the scaled arrival rate


# c. Mean number in the system (E[N])
E_N_original = rho_original / (1 - rho_original)  # Original mean number in the system
E_N_scaled = rho_scaled / (1 - rho_scaled)        # Scaled mean number in the system


# d. Mean time in the system (E[T])
E_T_original = 1 / (mu_original - lambda_original)  # Original mean time in the system
E_T_scaled = 1 / (mu_scaled - lambda_scaled)        # Scaled mean time in the system


# Plot the results
fig, axs = plt.subplots(2, 2, figsize=(14, 12))


# Plot Utilization (ρ)
axs[0, 0].plot(k_values, rho_scaled, label="Utilization (ρ)")
axs[0, 0].axhline(rho_original, color='red', linestyle='--', label="Original Utilization")
axs[0, 0].set_title("Utilization (ρ) vs Scaling Factor (k)")
axs[0, 0].set_xlabel("Scaling Factor (k)")
axs[0, 0].set_ylabel("Utilization (ρ)")
axs[0, 0].legend()
axs[0, 0].grid()


# Plot Throughput (X)
axs[0, 1].plot(k_values, throughput_scaled, label="Throughput (X)", color='orange')
axs[0, 1].set_title("Throughput (X) vs Scaling Factor (k)")
axs[0, 1].set_xlabel("Scaling Factor (k)")
axs[0, 1].set_ylabel("Throughput (X)")
axs[0, 1].legend()
axs[0, 1].grid()


# Plot Mean Number in the System (E[N])
axs[1, 0].plot(k_values, E_N_scaled, label="Mean Number in System (E[N])", color='green')
axs[1, 0].axhline(E_N_original, color='red', linestyle='--', label="Original E[N]")
axs[1, 0].set_title("Mean Number in System (E[N]) vs Scaling Factor (k)")
axs[1, 0].set_xlabel("Scaling Factor (k)")
axs[1, 0].set_ylabel("Mean Number (E[N])")
axs[1, 0].legend()
axs[1, 0].grid()


# Plot Mean Time in the System (E[T])
axs[1, 1].plot(k_values, E_T_scaled, label="Mean Time in System (E[T])", color='red')
axs[1, 1].axhline(E_T_original, color='blue', linestyle='--', label="Original E[T]")
axs[1, 1].set_title("Mean Time in System (E[T]) vs Scaling Factor (k)")
axs[1, 1].set_xlabel("Scaling Factor (k)")
axs[1, 1].set_ylabel("Mean Time (E[T])")
axs[1, 1].legend()
axs[1, 1].grid()


plt.tight_layout()
plt.show()
