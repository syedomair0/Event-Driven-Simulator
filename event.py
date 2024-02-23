# Packet Event Class
class Event:
    """
    Represents a packet event in the network simulation.
    """
    def __init__(self, time, source, destination):
        self.time = time
        self.source = source
        self.destination = destination

    def __lt__(self, other):
        return self.time < other.time
