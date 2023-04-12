import final_project_part1 as f
import part1 as p
import matplotlib.pyplot as plot

"""
import random
import min_heap
import matplotlib.pyplot as plot
"""


def experiment4_dijkstra(graph_size, min_edge, max_edge, max_k_value):
    total_dist = {}
    # Use this graph for all of the approximations
    G = f.create_random_complete_graph(graph_size, min_edge, max_edge)
    total_dist[0] = f.dijkstra(G, 0)

    # Calculates the approximate distance based on k value
    for i in range(max_k_value):
        total_dist[i + 1] = p.dijkstra_approx(G, 0, i + 1)

    # Calculates the sum of each distance
    for dicts in total_dist:
        total_sum = f.total_dist(total_dist.get(dicts))
        total_dist[dicts] = total_sum

    # Calculates the accuracy between Dijkstra and the approximations
    for k in range(1, max_k_value + 1):
        accuracy = (total_dist[0] / total_dist[k]) * 100
        total_dist[k] = accuracy
    total_dist[0] = 0

    # Graphs the accuracy between Dijkstra and the approximations
    plot.plot(total_dist.values())
    plot.title("Dijkstra vs Dijkstra Approximations With Varying K Values")
    plot.ylabel("Accuracy (%)")
    plot.xlabel("K Value")
    plot.show()

    return total_dist


def experiment4_bellman(graph_size, min_edge, max_edge, max_k_value):
    total_dist = {}
    # Use this graph for all of the approximations
    G = f.create_random_complete_graph(graph_size, min_edge, max_edge)
    total_dist[0] = f.bellman_ford(G, 0)

    # Calculates the approximate distance based on k value
    for i in range(max_k_value):
        total_dist[i + 1] = p.bellman_ford_approx(G, 0, i + 1)

    # Calculates the sum of each distance
    for dicts in total_dist:
        total_sum = f.total_dist(total_dist.get(dicts))
        total_dist[dicts] = total_sum

    # Calculates the accuracy between Dijkstra and the approximations
    for k in range(1, max_k_value + 1):
        accuracy = (total_dist[0] / total_dist[k]) * 100
        total_dist[k] = accuracy
    total_dist[0] = 0

    # Graphs the accuracy between Dijkstra and the approximations
    plot.plot(total_dist.values())
    plot.title("Bellman-Ford vs Bellman-Ford Approximations With Varying K Values")
    plot.ylabel("Accuracy (%)")
    plot.xlabel("K Value")
    plot.show()

    return total_dist


# experiment4_dijkstra(10, 1, 10, 9)
# experiment4_dijkstra(25, 1, 25, 24)
# experiment4_dijkstra(50, 1, 50, 49)

# experiment4_bellman(10, 1, 10, 9)
# experiment4_bellman(25, 1, 25, 24)
experiment4_bellman(50, 1, 50, 49)

"""
Optional print statement removed to improve run time

print("Accuracy of Dijkstra vs Dijkstra Approximation With k = " + str(k) + ",")
print(str(accuracy) + "%\n")
"""
