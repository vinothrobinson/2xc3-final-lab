import min_heap
import final_project_part1
import part1

G = final_project_part1.DirectedWeightedGraph()
for i in range(5):
    G.add_node(i)

G.add_edge(0, 1, 35)
G.add_edge(0, 2, 15)
G.add_edge(0, 3, 25)
G.add_edge(1, 0, 35)
G.add_edge(1, 2, 15)
G.add_edge(1, 4, 5)
G.add_edge(2, 0, 15)
G.add_edge(2, 1, 15)
G.add_edge(2, 3, 35)
G.add_edge(3, 0, 25)
G.add_edge(3, 2, 35)
G.add_edge(3, 4, 20)
G.add_edge(4, 1, 5)
G.add_edge(4, 2, 5)
G.add_edge(4, 3, 20)

print(final_project_part1.dijkstra(G, 0))
print(part1.dijkstra(G, 0, 1))
print(part1.dijkstra(G, 0, 2))