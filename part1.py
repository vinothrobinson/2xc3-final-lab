import min_heap


def dijkstra_approx(G, source, k):
    relaxed = {}
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        relaxed[node] = 0
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        # if current_element.key != float("-inf"):
        dist[current_node] = current_element.key

        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour] and relaxed[neighbour] < k:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
                relaxed[neighbour] += 1
                # if relaxed[neighbour] >= k:
                #     # Safely remove neighbour from Q
                #     Q.decrease_key(neighbour, float("-inf"))
                #     # finished_node = Q.extract_min().value
                #     print(f"Node {neighbour} was relaxed {k} times")
    return dist