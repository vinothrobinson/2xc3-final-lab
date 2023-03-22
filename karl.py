import final_project_part1 as f1
import part1 as f2
import matplotlib.pyplot as plot

def experiment1_gda(n):
    #k_values = [int(0.05 * (n - 1)), int(0.10 * (n - 1)), int(0.15 * (n - 1))]
    k_values = [1, 2, 3]
    final_list = [[], [], []]
    x_axis = []

    for edges in range(n, (2 * f1.triangle(n - 1)) + 1):
        x_axis.append(edges)
        G = f1.create_random_graph(n, edges, 1, 100)
        shortest_paths = f1.dijkstra(G, 0)
        shortest_path = sum(shortest_paths.values())
        for index in range(len(k_values)):
            approx_paths = f2.dijkstra_approx(G, 0, k_values[index])
            approx_path = sum(approx_paths.values())
            final_list[index].append(shortest_path / approx_path * 100)

    for index in range(len(k_values)):
        plot.plot(x_axis, final_list[index], label="k = " + str(k_values[index]))
    plot.xlabel("Graph density (measured in number of edges)")
    plot.ylabel("Accuracy of approximation")
    plot.title("Ice Spikes Biome")
    plot.legend()
    plot.show()

experiment1_gda(15)