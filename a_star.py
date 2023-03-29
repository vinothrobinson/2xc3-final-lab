import final_project_part1 as p1
import min_heap

def a_star(G, s, d, h):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    '''marked = {}'''
    shortest_path = []
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        '''marked[node] = False'''
    Q.decrease_key(s, h(s))

    while not Q.is_empty():
        current_element = Q.extract_min()
        if current_element.value == d:
            shortest_path.append(d)
            '''print(marked)
            print(pred)
            print(shortest_path)'''
            return (pred, shortest_path)
        shortest_path.append(current_element.value)
        '''marked[current_element.value] = True'''
        current_node = current_element.value
        dist[current_node] = current_element.key - h(current_node)
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h(neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    '''print(marked)
    print(pred)'''
    return (pred, shortest_path)

def h(node):
    heur = {'A': 9, 'B': 7, 'C': 8, 'D': 7, 'E': 0, 'F': 6, 'G': 3, 'H': 6, 'I': 4, 'J': 4, 'K': 3, 'L': 6, 'S': 10}
    return heur[node]

G = p1.DirectedWeightedGraph()
in_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "S"]
for node in in_list:
    G.add_node(node)
G.add_edge("S", "A", 7)
G.add_edge("A", "S", 7)
G.add_edge("S", "B", 2)
G.add_edge("B", "S", 2)
G.add_edge("S", "C", 3)
G.add_edge("C", "S", 3)
G.add_edge("A", "B", 3)
G.add_edge("B", "A", 3)
G.add_edge("B", "D", 4)
G.add_edge("D", "B", 4)
G.add_edge("A", "D", 4)
G.add_edge("D", "A", 4)
G.add_edge("B", "H", 1)
G.add_edge("H", "B", 1)
G.add_edge("H", "F", 3)
G.add_edge("F", "H", 3)
G.add_edge("D", "F", 5)
G.add_edge("F", "D", 5)
G.add_edge("H", "G", 2)
G.add_edge("G", "H", 2)
G.add_edge("C", "L", 2)
G.add_edge("L", "C", 2)
G.add_edge("L", "I", 4)
G.add_edge("I", "L", 4)
G.add_edge("L", "J", 4)
G.add_edge("J", "L", 4)
G.add_edge("I", "J", 7)
G.add_edge("J", "I", 6)
G.add_edge("I", "K", 4)
G.add_edge("K", "I", 4)
G.add_edge("J", "K", 4)
G.add_edge("K", "J", 4)
G.add_edge("K", "E", 5)
G.add_edge("E", "K", 5)
G.add_edge("G", "E", 2)
G.add_edge("E", "G", 2)

test_case = a_star(G, "S", "E", h)
print("Predecessor Dictionary: " + str(test_case[0]))
print("Shortest Path : " + str(test_case[1]))