import unittest
from unittest.mock import patch
from network import Network
from event import Event
from scheduler import Scheduler



class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.network = Network(n=10, m=2)  # Small graph for testing

    @patch('network.nx.dijkstra_path_length', return_value=5)
    def test_route_packet_success(self, mock_path_length):
        event = Event(time=1, source=0, destination=1)
        self.network.route_packet(event)
        self.assertEqual(self.network.packet_transmissions, 1)
        self.assertEqual(self.network.packet_successes, 1)
        self.assertIn(5, self.network.latencies)

class TestEvent(unittest.TestCase):
    def test_initialization(self):
        event = Event(time=1, source=0, destination=5)
        self.assertEqual(event.time, 1)
        self.assertEqual(event.source, 0)
        self.assertEqual(event.destination, 5)

    def test_lt_comparison(self):
        event1 = Event(time=1, source=0, destination=5)
        event2 = Event(time=2, source=3, destination=4)
        self.assertTrue(event1 < event2)
        self.assertFalse(event2 < event1)

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()

    def test_initialization(self):
        self.assertTrue(self.scheduler.event_queue.empty())

    def test_schedule_and_get_next_event(self):
        event1 = Event(time=2, source=0, destination=1)
        event2 = Event(time=1, source=1, destination=0)
        self.scheduler.schedule_event(event1)
        self.scheduler.schedule_event(event2)
        # Ensure events are retrieved in correct order
        self.assertEqual(self.scheduler.get_next_event(), event2)
        self.assertEqual(self.scheduler.get_next_event(), event1)

    def test_get_next_event_empty_queue(self):
        self.assertIsNone(self.scheduler.get_next_event())

if __name__ == '__main__':
    unittest.main()


