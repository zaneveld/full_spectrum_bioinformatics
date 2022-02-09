#!/usr/bin/env python
from __future__ import division

__author__ = ""
__copyright__ = ""
__credits__ = []
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = ""
__email__ = "yourname@gmail.com"
__status__ = "Development"

from unittest import TestCase, main
from random_network import NetworkNode

class NetworkNodeTests(TestCase):
    """ """

    def setUp(self):
        n1 = NetworkNode(name="geneA",edges=[])
        n2 = NetworkNode(name="geneB",edges=[])
        n3 = NetworkNode(name="geneC",edges=[n1,n2])
        self.SimpleNetwork = [n1,n2,n3]

    def test_add_edge(self):
        """Adding an edge adds exactly one edge"""
        n1,n2,n3 = self.SimpleNetwork
        n2.addEdge(n1)
        n2_connections = [edge.Name for edge in n2.Edges]
        obs = n2_connections
        exp = ["geneC","geneA"]
        self.assertEqual(obs,exp)

    def test_degree_works_with_normal_inputs(self):
        """Node.degree calculates node degree in normal circumstances"""
        n1,n2,n3 = self.SimpleNetwork
        obs = n3.degree()
        exp = 2
        self.assertEqual(obs,exp)

if __name__ == "__main__":
    main()
