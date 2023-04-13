import math
import final_project_part1
import part1
import part1
import timeit
import matplotlib.pyplot as plot

import refactor


def experiment1_data(func, func_approx, node_num, trial_num, lower_bound = 1, ks = [0.05, 0.1, 0.25, 0.5]):
    avg_times = [[] for i in range(len(ks) + 1)]

    for edge_num in range(node_num, 2 * final_project_part1.triangle(node_num-1) + 1):
        times = [0 for _ in range(len(ks) + 1)]
        for _ in range(trial_num):
            G = final_project_part1.create_random_graph(node_num, edge_num, lower_bound, 1000)

            start_time = timeit.default_timer()
            func(G, 0, 7)
            end_time = timeit.default_timer()

            times[0] += end_time - start_time

            for i, k in enumerate(ks):
                start_time = timeit.default_timer()
                func_approx(G, 0, k * node_num)
                end_time = timeit.default_timer()

                times[i+1] += end_time - start_time

        for i in range(len(ks) + 1):
            avg_times[i].append(times[i] / trial_num)

    return avg_times


def experiment1_graph(data, node_num, name, ks=[0.05, 0.1, 0.25, 0.5]):
    plot.title(f"Graph Density vs Run Time of Approximations\nfor Various K-Values (|V| = {node_num})")
    plot.xlabel("Graph Density")
    plot.ylabel("Run Time")
    plot.plot(list(range(node_num, 2 * final_project_part1.triangle(node_num - 1) + 1)), data[0], label=name)
    for i, k in enumerate(ks):
        plot.plot(list(range(node_num, 2 * final_project_part1.triangle(node_num - 1) + 1)), data[i+1], label=f"{name} Approximation (k={math.ceil(k*node_num)})")
    plot.legend()
    plot.show()


# data = experiment1_data(final_project_part1.dijkstra, part1.dijkstra_approx, 10, 10, ks=[0.1, 0.2, 0.5])
# experiment1_graph(data, 10, "Dijkstra", ks=[0.1, 0.2, 0.5])

# data = experiment1_data(final_project_part1.dijkstra, part1.dijkstra_approx, 20, 10)
# experiment1_graph(data, 20, "Dijkstra")
#
# data = experiment1_data(final_project_part1.dijkstra, part1.dijkstra_approx, 30, 10)
# experiment1_graph(data, 30, "Dijkstra")


# data = experiment1_data(final_project_part1.bellman_ford, part1.bellman_ford_approx, 10, 10, ks=[0.1, 0.2, 0.5])
# experiment1_graph(data, 10, "Bellman-Ford", ks=[0.1, 0.2, 0.5])

# data = experiment1_data(final_project_part1.bellman_ford, part1.bellman_ford_approx, 20, 10)
# experiment1_graph(data, 20, "Bellman-Ford")
#
# data = experiment1_data(final_project_part1.bellman_ford, part1.bellman_ford_approx, 30, 10)
# experiment1_graph(data, 30, "Bellman-Ford")


def experiment2_data(n, funcs, approx_funcs, func_names): #gda graph
    k_values = [1, 2, 3]
    final_list = [[], [], []]
    x_axis = []

    for i in range(len(funcs)):
        for edges in range(n, (2 * final_project_part1.triangle(n - 1)) + 1):
            x_axis.append(edges)
            G = final_project_part1.create_random_graph(n, edges, 1, 100)
            shortest_paths = funcs[i](G, 0)
            shortest_path = sum(shortest_paths.values())
            for index in range(len(k_values)):
                approx_paths = approx_funcs[i](G, 0, k_values[index])
                approx_path = sum(approx_paths.values())
                final_list[index].append(shortest_path / approx_path * 100)

        for index in range(len(k_values)):
            plot.plot(x_axis, final_list[index], label="k = " + str(k_values[index]))
        plot.xlabel("Graph Density (measured in number of edges)")
        plot.ylabel("Accuracy of Approximation")
        plot.title("Accuracy vs. Density: " + func_names[i])
        plot.legend()
        plot.show()
        plot.close()

        final_list = [[], [], []]
        x_axis = []

#experiment2_data(30, [final_project_part1.dijkstra, final_project_part1.bellman_ford], [part1.dijkstra_approx, part1.bellman_ford_approx], ["Dijkstra", "Bellman-Ford"])