from queue import PriorityQueue

# Event Scheduler Class
class Scheduler:
    """
    Manages scheduling and processing of events in the simulation.
    """
    def __init__(self):
        self.event_queue = PriorityQueue()

    def schedule_event(self, event):
        self.event_queue.put(event)

    def get_next_event(self):
        if not self.event_queue.empty():
            return self.event_queue.get()
        else:
            return None
