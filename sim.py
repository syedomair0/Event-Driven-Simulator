import matplotlib.pyplot as plt
import time
import pandas as pd

from network import Network

# Simulation parameters
num_simulations = 10
num_packets_per_simulation = 50
n = 100  # Number of nodes
m = 2    # Number of edges to attach from a new node to existing nodes for Barabási-Albert model

# Data collection variables
event_handling_times = []
avg_packet_processing_times = []
network_throughputs = []
packet_loss_rates = []
latencies = []

for _ in range(100):
    start_time = time.time()
    simulator = Network(model="barabasi_albert", n=n, m=m)
    # Measure event handling efficiency
    simulator.run_simulation(num_packets=num_packets_per_simulation)
    end_time = time.time()
    event_handling_time = (end_time - start_time) / num_packets_per_simulation
    
    # Calculate packet loss rate
    packet_loss_rate = 1 - (simulator.packet_successes / simulator.packet_transmissions)
    
    # Calculate average packet processing time (simplified as average latency here)
    avg_packet_processing_time = simulator.total_latency / simulator.packet_successes if simulator.packet_successes > 0 else float('inf')
    
    # Network throughput (packets successfully delivered)
    network_throughput = simulator.packet_successes
    
    # Collect data points
    event_handling_times.append(event_handling_time)
    avg_packet_processing_times.append(avg_packet_processing_time)
    network_throughputs.append(network_throughput)
    packet_loss_rates.append(packet_loss_rate)

# Calculate summary statistics for latency
latency_df = pd.DataFrame(simulator.latencies, columns=['Latency'])
latency_summary = latency_df.describe()

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Network Simulation Metrics')

# Event Handling Efficiency
axs[0, 0].plot(event_handling_times, marker='o', linestyle='-')
axs[0, 0].set_title('Event Handling Efficiency')
axs[0, 0].set_xlabel('Simulation #')
axs[0, 0].set_ylabel('Time per Event (s)')

# Average Packet Processing Time
axs[0, 1].plot(avg_packet_processing_times, marker='o', linestyle='-')
axs[0, 1].set_title('Average Packet Processing Time')
axs[0, 1].set_xlabel('Simulation #')
axs[0, 1].set_ylabel('Time (s)')

# Network Throughput
axs[1, 0].plot(network_throughputs, marker='o', linestyle='-')
axs[1, 0].set_title('Network Throughput')
axs[1, 0].set_xlabel('Simulation #')
axs[1, 0].set_ylabel('Packets Delivered')

# Packet Loss Rate
axs[1, 1].plot(packet_loss_rates, marker='o', linestyle='-')
axs[1, 1].set_title('Packet Loss Rate')
axs[1, 1].set_xlabel('Simulation #')
axs[1, 1].set_ylabel('Loss Rate')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Print latency distribution summary
print("Latency Distribution Summary:")
print(latency_summary)
