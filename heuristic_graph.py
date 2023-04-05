import a_star


class HeuristicGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}
        self.heuristic = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        if node1 not in self.adj[node2]:
            self.adj[node2].append(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)

    def get_heuristic(self):
        return self.heuristic

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic


def a_star_heuristic(G, s, d):
    return a_star.a_star(G, s, d, lambda n: G.get_heuristic()[(n, d)])
