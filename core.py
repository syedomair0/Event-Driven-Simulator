import heapq
import random
import networkx as nx

# Enhanced Event Class
class Event:
    def __init__(self, event_type, time, source=None, destination=None, packet_size=0):
        self.event_type = event_type  # "arrival" or "departure"
        self.time = time
        self.source = source
        self.destination = destination
        self.packet_size = packet_size

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
        self.graph = None

    def generate_topology(self, model="BarabasiAlbert", **kwargs):
        if model == "BarabasiAlbert":
            self.graph = nx.barabasi_albert_graph(kwargs['n'], kwargs['m'])
        elif model == "Waxman":
            self.graph = nx.waxman_graph(kwargs['n'], alpha=kwargs.get('alpha', 0.4), beta=kwargs.get('beta', 0.1))
        else:
            raise ValueError("Unsupported network model")

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

# Initializing the scheduler and network with a specific topology
scheduler = Scheduler()
network = Network()

# Example: Generate Barabasi-Albert topology
network.generate_topology("BarabasiAlbert", n=100, m=2)

# Generate initial events with network context
initialize_events(scheduler, num_events=100, network=network)

# Run the enhanced simulation loop
run_simulation(scheduler, network)

"Simulation setup with enhanced functionality including network topology generation and event processing."

