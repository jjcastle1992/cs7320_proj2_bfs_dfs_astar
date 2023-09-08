from unittest import TestCase
from genGraphAsDict import build_graph_as_dict

# TESTs for creating Graph Data Structure (Python dict)
# Recommend working on directed graph first, then uncomment 2nd test fn for undirected graph

class Test(TestCase):

    def test_build_directed_graph_as_dict(self):
        node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]

        graph_dict = build_graph_as_dict(node_list, directed_graph=True)

        # test that a key exists for each of the first nodes in node_list tuples (from->to)
        assert ('A' in graph_dict.keys()) == True
        assert ('B' in graph_dict.keys()) == True
        assert ('C' in graph_dict.keys()) == True

        # Test expected number of keys in graph_dict
        assert len(graph_dict) == 3

        # test that we have correct children for 'C'
        child_list = graph_dict['C']
        assert ('D' in child_list) == True
        assert ('E' in child_list) == True

        print ("Passed all tests")


''' Uncomment this test when you have implemented for undirected graphs

    def test_build_UNdirected_graph_as_dict(self):
        node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('A', 'E'), ('B', 'F')]

        graph_dict = build_graph_as_dict(node_list, isDirectedGraph=False)

        # test that a key exists for each of the first nodes in node_list tuples (from->to)
        assert ('A' in graph_dict.keys()) == True
        assert ('B' in graph_dict.keys()) == True
        assert ('C' in graph_dict.keys()) == True
        assert ('D' in graph_dict.keys()) == True
        assert ('E' in graph_dict.keys()) == True
        assert ('F' in graph_dict.keys()) == True

        # Test expected number of keys in graph_dict
        assert len(graph_dict)  == 6

        # test that we have correct children for 'C'
        child_list = graph_dict['C']
        assert ('D' in child_list) == True
        assert ('E' in child_list) == True
        assert ('B' in child_list) == True

        # test that we have correct children for 'F'
        child_list = graph_dict['F']
        assert ('B' in child_list) == True
        
        print ("Passed all tests")
'''
