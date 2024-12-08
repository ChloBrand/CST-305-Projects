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
