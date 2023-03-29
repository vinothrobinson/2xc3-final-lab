import final_project_part1 as f1
import part1 as f2
import matplotlib.pyplot as plot

def experiment1_gda(n, functions):
    k_values = [1, 2, 3]
    final_list = [[], [], []]
    x_axis = []

    for _ in range(len(functions)):
        for edges in range(n, (2 * f1.triangle(n - 1)) + 1):
            x_axis.append(edges)
            G = f1.create_random_graph(n, edges, 1, 100)
            shortest_paths = f1.dijkstra(G, 0)
            shortest_path = sum(shortest_paths.values())
            for index in range(len(k_values)):
                approx_paths = f2.dijkstra_approx(G, 0, k_values[index])
                approx_path = sum(approx_paths.values())
                final_list[index].append(shortest_path / approx_path * 100)

    #for index in range(len(k_values)):

    plot.plot(x_axis, final_list[0], label="k = " + str(k_values[0]))
    plot.plot(x_axis, final_list[1], label="k = " + str(k_values[1]))
    plot.plot(x_axis, final_list[2], label="k = " + str(k_values[2]))
    plot.xlabel("Graph density (measured in number of edges)")
    plot.ylabel("Accuracy of approximation")
    plot.title("Ice Spikes Biome")
    plot.legend()
    plot.show()

experiment1_gda(15, [1, 1])