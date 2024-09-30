from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(dict)

    def add_edge(self, node1, node2, weight=1):
        self.edges[node1][node2] = weight
        self.edges[node2][node1] = weight

    def get_neighbors(self, node):
        return self.edges.get(node, {})

    def remove_edge(self, node1, node2):
        if node2 in self.edges[node1]:
            del self.edges[node1][node2]
        if node1 in self.edges[node2]:
            del self.edges[node2][node1]

    def get_all_nodes(self):
        return list(self.edges.keys())