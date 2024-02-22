import heapq
import random
import networkx as nx

# Enhanced Event Class
class Event:
    def __init__(self, event_type, time, source=None, destination=None, packet_size=0, path=None):
        self.event_type = event_type  # "arrival", "transmission", or "departure"
        self.time = time
        self.source = source
        self.destination = destination
        self.packet_size = packet_size  # in bytes
        self.path = path  # for packet forwarding

    def __lt__(self, other):
        return self.time < other.time


# Enhanced Scheduler Class
class Scheduler:
    def __init__(self):
        self.queue = []

    def schedule_event(self, event):
        heapq.heappush(self.queue, event)

    def get_next_event(self):
        return heapq.heappop(self.queue) if self.queue else None

# Enhanced Network Class with topology generation methods
class Network:
    def __init__(self):
        self.graph = nx.Graph()
        self.links = {}  # Dictionary for link properties

    def generate_topology(self, model="BarabasiAlbert", **kwargs):
        if model == "BarabasiAlbert":
            self.graph = nx.barabasi_albert_graph(kwargs['n'], kwargs['m'])
        elif model == "Waxman":
            self.graph = nx.waxman_graph(kwargs['n'], alpha=kwargs.get('alpha', 0.4), beta=kwargs.get('beta', 0.1))
        else:
            raise ValueError("Unsupported network model")

        # Initialize links with default properties
        for u, v in self.graph.edges():
            self.links[(u, v)] = Link(bandwidth=np.random.uniform(10, 100), latency=np.random.uniform(1, 10))
            self.links[(v, u)] = self.links[(u, v)]  # Assuming symmetrical links

    def add_link(self, source, destination, bandwidth, latency):
        self.links[(source, destination)] = Link(bandwidth, latency)
        self.links[(destination, source)] = Link(bandwidth, latency)  # Symmetrical link

    def get_link_properties(self, source, destination):
        return self.links.get((source, destination), None)


# Global simulation time
global_time = 0

# Enhance initialization and event generation with network simulation
def initialize_events(scheduler, num_events=100, network=None):
    if not network or not network.graph:
        print("Network topology is not initialized.")
        return
    nodes = list(network.graph.nodes)
    for _ in range(num_events):
        event_type = random.choice(["arrival", "departure"])
        time = random.uniform(0, 100)
        source, destination = random.sample(nodes, 2)
        packet_size = random.randint(64, 1500)  # Random packet size in bytes
        scheduler.schedule_event(Event(event_type, time, source, destination, packet_size))

# Enhanced simulation loop
def run_simulation(scheduler, network):
    global global_time
    while scheduler.queue:
        event = scheduler.get_next_event()
        global_time = event.time
        # Example processing logic
        if event.event_type == "arrival":
            # For simplicity, assuming packet is instantly processed and departed
            print(f"Packet arrived from {event.source} to {event.destination} at {event.time}, size={event.packet_size} bytes")
        global_time = event.time  # Advance global time

def simulate_packet_arrival(scheduler, network, num_packets=100):
    """Simulate packet arrival events and schedule them."""
    nodes = list(network.graph.nodes())
    for _ in range(num_packets):
        source = random.choice(nodes)
        destination = random.choice(nodes)
        while destination == source:
            destination = random.choice(nodes)  # Ensure source and destination are different
        packet_size = random.randint(64, 1500)  # Packet size in bytes
        event_time = random.uniform(0, 100)  # Random arrival time
        scheduler.schedule_event(Event("arrival", event_time, source, destination, packet_size))

def simulate_packet_forwarding(scheduler, event, network):
    """Simulate packet forwarding based on routing information."""
    if event.event_type == "arrival":
        # Here we would implement a routing algorithm, for simplicity we use shortest path
        path = nx.shortest_path(network.graph, source=event.source, target=event.destination)
        event.path = path  # Update event with calculated path for packet
        # Calculate total latency based on the path
        total_latency = sum(network.get_link_properties(path[i], path[i+1]).latency for i in range(len(path)-1))
        # Schedule a departure event after processing latency
        scheduler.schedule_event(Event("departure", event.time + total_latency, event.source, event.destination, event.packet_size, path))

def run_simulation_with_routing(scheduler, network):
    while scheduler.queue:
        event = scheduler.get_next_event()
        global global_time
        global_time = event.time  # Advance global simulation time to the event time
        if event.event_type == "arrival":
            simulate_packet_forwarding(scheduler, event, network)
        elif event.event_type == "departure":
            print(f"Packet from {event.source} to {event.destination} forwarded at {event.time}, size={event.packet_size} bytes, path={event.path}")

# Initializing the scheduler and network with a specific topology
scheduler = Scheduler()
network = Network()

# Example: Generate Barabasi-Albert topology
network.generate_topology("BarabasiAlbert", n=100, m=2)

# Generate initial events with network context
initialize_events(scheduler, num_events=100, network=network)

# Run the enhanced simulation loop
run_simulation(scheduler, network)

# Simulating packet arrival events
simulate_packet_arrival(scheduler, network, num_packets=100)

# Running the simulation with packet forwarding and routing
run_simulation_with_routing(scheduler, network)
