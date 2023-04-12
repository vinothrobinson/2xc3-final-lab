# ----------- Refactoring The Code ---------------
from typing import List, Dict, Callable
from abc import ABC, abstractmethod
import min_heap


# This file will outline how to refactor the code.
# ----------------------- Graphs --------------------------
class Graph(ABC):
    @abstractmethod
    def get_adj_nodes(self, node: int) -> List[int]:
        return

    @abstractmethod
    def add_node(self, node: int):
        return

    @abstractmethod
    def add_edge(self, start: int, end: int, weight: float):
        return

    @abstractmethod
    def w(self, node1: int, node2: int) -> float:
        return

    @abstractmethod
    def get_num_of_nodes(self) -> int:
        return


class WeightedGraph(Graph):
    def __init__(self):
        self.adj = {}
        self.weights = {}

    def get_adj_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def get_num_of_nodes(self) -> int:
        return len(self.adj)

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False


class HeuristicGraph(WeightedGraph):
    _heuristic: Dict[int, int]

    def __init__(self, heuristic: Dict[int, int]):
        self._heuristic = heuristic

    def get_heuristic(self):
        return self._heuristic


# ----------------------- Algorithms --------------------------
class Algorithm(ABC):
    @staticmethod
    @abstractmethod
    def calc_sp(graph: Graph, source: int, dest: int) -> float:
        return


class Dijkstra(Algorithm):
    @staticmethod
    def calc_sp(graph: Graph, source: int, dest: int) -> float:
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        Q = min_heap.MinHeap([])
        nodes = list(graph.adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        # Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node
        return dist[dest]


class Bellman_Ford(Algorithm):
    @staticmethod
    def calc_sp(graph: Graph, source: int, dest: int) -> float:
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        nodes = list(graph.adj.keys())

        # Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        # Meat of the algorithm
        for _ in range(graph.get_num_of_nodes()):
            for node in nodes:
                for neighbour in graph.adj[node]:
                    if dist[neighbour] > dist[node] + graph.w(node, neighbour):
                        dist[neighbour] = dist[node] + graph.w(node, neighbour)
                        pred[neighbour] = node
        return dist[dest]


class A_Star_Adapter(Algorithm):
    @staticmethod
    def calc_sp(graph: Graph, source: int, dest: int, h: Callable[[int], float]) -> float:
        _heuristic = {}
        for node1 in graph.adj:
            _heuristic[node1] = h(node1)
        return A_Star.calc_sp(graph, source, dest, _heuristic)


class A_Star(Algorithm):
    @staticmethod
    def calc_sp(graph: Graph, source: int, dest: int, heuristic: Dict[int, float]):
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        shortest_path = []
        Q = min_heap.MinHeap([])
        nodes = list(graph.adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")

        Q.decrease_key(source, heuristic[source])

        while not Q.is_empty():
            current_element = Q.extract_min()
            if current_element.value == dest:
                shortest_path.append(dest)
                return dist[dest] #(pred, shortest_path)
            shortest_path.append(current_element.value)
            current_node = current_element.value
            dist[current_node] = current_element.key - heuristic[current_node]
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour,
                                   dist[current_node] + graph.w(current_node, neighbour) + heuristic[neighbour])
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node
        return dist[dest]


# ----------------------- Algorithms --------------------------
class ShortPathFinder():

    def __init__(self, graph: Graph, algorithm: Algorithm):
        self.graph = graph
        self.algorithm = algorithm

    def set_algorithm(self, algorithm: Algorithm):
        self.algorithm = algorithm

    def set_graph(self, graph: Graph):
        self.graph = graph

    def calc_shortest_path(self, source: int, dest: int) -> float:
        return self.algorithm.calc_sp(self.graph, source, dest)
