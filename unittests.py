import unittest
from network import Network, Node, Link

class TestNetwork(unittest.TestCase):
    def test_network_initialization_barabasi_albert(self):
        parameters = {'n': 100, 'm': 2}
        network = Network(model='BarabasiAlbert', parameters=parameters)
        self.assertEqual(len(network.graph.nodes), 100)
        self.assertEqual(len(network.graph.edges), (100 - 2) * 2)

    def test_network_initialization_waxman(self):
        parameters = {'n': 100, 'alpha': 0.1, 'beta': 0.1}
        network = Network(model='Waxman', parameters=parameters)
        self.assertEqual(len(network.graph.nodes), 100)
        # Waxman graph edges are less predictable, so we test for existence
        self.assertTrue(len(network.graph.edges) > 0)

    def test_invalid_network_model(self):
        parameters = {'n': 100, 'm': 2}
        with self.assertRaises(ValueError):
            Network(model='InvalidModel', parameters=parameters)

class TestNode(unittest.TestCase):
    def test_node_initialization(self):
        node = Node(node_id=1)
        self.assertEqual(node.node_id, 1)

class TestLink(unittest.TestCase):
    def test_link_initialization(self):
        link = Link(source=1, destination=2, bandwidth=100, latency=10)
        self.assertEqual(link.source, 1)
        self.assertEqual(link.destination, 2)
        self.assertEqual(link.bandwidth, 100)
        self.assertEqual(link.latency, 10)

if __name__ == '__main__':
    unittest.main()

