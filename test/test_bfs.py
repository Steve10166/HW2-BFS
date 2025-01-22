# write tests for bfs
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))#added to modify python path to root dir.
from search import graph
import networkx as nx



def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    tiny_graph = graph.Graph("data/tiny_network.adjlist")
    tiny = tiny_graph.bfs("31806696")

    # result = tiny.bfs('Martin Kampmann', '31540829')
    
    assert tiny is not None #test got correct number of nodes
    assert len(tiny) == 30, (
        f"Traversal should include 30 nodes, but got {len(tiny)}"
    )

    order = tiny_graph.bfs("31806696", "Martin Kampmann") #test return in correct order
    #print(order)
    assert order == ['31806696', 'Luke Gilbert', '33483487', 'Martin Kampmann']
    shortestpath = tiny_graph.bfs('31806696')
    print(shortestpath)


    pass

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    citation = graph.Graph("data/citation_network.adjlist")

    # Test shortest path
    path = citation.bfs("Luke Gilbert", "Tony Capra")
    print(path)
    assert citation.bfs("Luke Gilbert", "Tony Capra") is not None
    
    assert citation.bfs("Hani Goodarzi", "Steven Brenner") is not None

    shortestpath = citation.bfs('Steven Brenner', 'Neil Risch')
    print(shortestpath)
    assert shortestpath == ['Steven Brenner', '31564432', 'Neil Risch']

    

    # Test BFS traversal
    traversal_result = citation.bfs("Luke Gilbert")
    assert traversal_result is not None
    assert len(traversal_result) > 0  # Ensure nodes are traversed

    # Test edge cases
    try:
        citation.bfs("Nonexistent")
    except ValueError as e:
        assert str(e) == "Start node Nonexistent does not exist in the graph."
    #end on nonexistent node
    assert citation.bfs("Luke Gilbert", "Nonexistent Node") is None

    #test empty graph 
    empty = graph.Graph("data/empty.adjlist")

    try:
        empty.bfs("A")
    except ValueError as e:
        assert str(e) == "Start node A does not exist in the graph."

    unconnected_graph = graph.Graph("data/unconn.adjlist")

    # Test BFS traversal from a node in one component
    traversal_result = unconnected_graph.bfs("A", "B")
    assert traversal_result == ["A", "B"]

    # Test BFS with end node in a different component
    assert unconnected_graph.bfs("A", "C") is None  # No path between components


    


    


test_bfs_traversal()