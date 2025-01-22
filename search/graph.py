import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if start not in self.graph:
            raise ValueError(f"Start node {start} does not exist in the graph.")

        visited = set()  # To track visited nodes
        traversal_order = []  # To store traversal order
        queue = [[start]]  # Queue to store paths

        while queue:
            path = queue.pop(0)  # Dequeue the first path
            node = path[-1]  # Get the last node in the path

            if node not in visited:
                visited.add(node)
                traversal_order.append(node)  # Maintain traversal order

                if end is not None and node == end:
                    return path  # Return the shortest path when `end` is reached

                for neighbor in self.graph.neighbors(node):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)

        if end is not None:
            return None  # If no path to `end` is found
        return traversal_order




