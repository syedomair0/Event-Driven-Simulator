import networkx as nx
import numpy as np
from scheduler import Scheduler
from event import Event

# Network Simulation Class
class Network:
    """
    Represents the network simulation, including the network graph, event scheduling, and statistics.
    """
    def __init__(self, model="barabasi_albert", n=200, m=5):
        if model == "barabasi_albert":
            self.graph =  nx.barabasi_albert_graph(n, m)
        elif model == "waxman":
            self.graph = nx.waxman_graph(n, alpha=0.4, beta=0.1)
        else:
            raise ValueError("Unsupported network model")

        for (u, v) in self.graph.edges():
            self.graph.edges[u, v]['latency'] = np.random.randint(1, 10)  # Example: latency between 1 and 10 units

        self.scheduler = Scheduler()
        self.packet_transmissions = 0
        self.packet_successes = 0
        self.total_latency = 0
        self.latencies = []  # Use this to collect individual packet latencies


    def route_packet(self, event):
        """
        Simulates routing a packet from source to destination and collects statistics.
        """
        try:
            if event.source not in self.graph or event.destination not in self.graph:
                raise nx.NodeNotFound("Source or destination node not found in the graph.")
            #path = nx.shortest_path(self.graph, source=event.source, target=event.destination)
            path_length = nx.dijkstra_path_length(self.graph, source=event.source, target=event.destination, weight='latency')

            self.packet_transmissions += 1
            self.packet_successes += 1
            #latency += len(path) - 1
            self.latencies.append(path_length)  # Collect individual latency
            #self.latencies.append(latency)  # Collect individual latency
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            self.packet_transmissions += 1

    def update_topology(self):
        """
        Simulates dynamic changes in the network topology.
        """
        if np.random.rand() > 0.5:  # Randomly choose to update the topology or not
            if np.random.rand() > 0.5 and self.graph.number_of_nodes() > 2:
                node_to_remove = np.random.choice(list(self.graph.nodes()))
                self.graph.remove_node(node_to_remove)
            else:
                new_node = max(self.graph.nodes()) + 1
                node_to_connect = np.random.choice(list(self.graph.nodes()))
                self.graph.add_edge(new_node, node_to_connect)

    def run_simulation(self, events=100):
        """
        Runs the network simulation with a specified number of packet events.
        """
        for _ in range(events):
            time = np.random.randint(1, 100)
            source = np.random.randint(0, 100)
            destination = np.random.randint(0, 100)
            if source != destination:
                self.scheduler.schedule_event(Event(time, source, destination))

        while True:
            event = self.scheduler.get_next_event()
            if event is None:  # No more events to process
                break
            self.route_packet(event)
            self.update_topology()

        # Calculate and print performance statistics
        self.total_latency = sum(self.latencies)
        average_latency = self.total_latency / len(self.latencies) if self.latencies else 0
        print(f"Total Latency: {self.total_latency}, Average Latency: {average_latency}")

        success_rate = self.packet_successes / self.packet_transmissions if self.packet_transmissions > 0 else 0
        print(f"Simulation complete. Success Rate: {success_rate:.2f}, Average Latency: {average_latency:.2f}")
