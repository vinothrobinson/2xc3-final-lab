import final_project_part1 as f
import matplotlib.pyplot as plot
import min_heap
import random

def dijkstra_all_pairs(num_nodes, min_edge, max_edge):
    n = num_nodes
    matrix = [[0]* n for index in range(n)]
    matrix[0][0] = 0
    total_dist = {}
    G = f.create_random_complete_graph(num_nodes, min_edge, max_edge)
    for i in range(n):
        total_dist[i] = f.dijkstra(G, i)
    # print(total_dist)
    for i in total_dist[i]:
        k = 0
        for j in total_dist[i].values():
            matrix[i][k] = j
            k += 1
    print("Dijkstra All Pairs")
    for m in matrix:
        print(m)
    print("\n")
    return

def bellman_all_pairs(num_nodes, min_edge, max_edge):
    n = num_nodes
    matrix = [[0]* n for index in range(n)]
    matrix[0][0] = 0
    total_dist = {}
    G = f.create_random_complete_graph(num_nodes, min_edge, max_edge)
    for i in range(n):
        total_dist[i] = f.bellman_ford(G, i)
    # print(total_dist)
    for i in total_dist[i]:
        k = 0
        for j in total_dist[i].values():
            matrix[i][k] = j
            k += 1
    print("Bellman-Ford All Pairs")
    for m in matrix:
        print(m)
    print("\n")
    return

dijkstra_all_pairs(10, 1, 10)
bellman_all_pairs(10, 1, 10)