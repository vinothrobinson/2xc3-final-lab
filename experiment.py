import math
import final_project_part1 as f
import approx as a
import timeit
import matplotlib.pyplot as plot
from tqdm import tqdm

# --------------------------------------- Experiment 1 ---------------------------------------------
def experiment1_data(func, func_approx, node_num, trial_num, lower_bound = 1, ks = [0.05, 0.1, 0.25, 0.5]):
    avg_times = [[] for i in range(len(ks) + 1)]

    for edge_num in range(node_num, 2 * f.triangle(node_num-1) + 1):
        times = [0 for _ in range(len(ks) + 1)]
        for _ in range(trial_num):
            G = f.create_random_graph(node_num, edge_num, lower_bound, 1000)

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
    plot.plot(list(range(node_num, 2 * f.triangle(node_num - 1) + 1)), data[0], label=name)
    for i, k in enumerate(ks):
        plot.plot(list(range(node_num, 2 * f.triangle(node_num - 1) + 1)), data[i+1], label=f"{name} Approximation (k={math.ceil(k*node_num)})")
    plot.legend()
    plot.show()


# data = experiment1_data(f.dijkstra, a.dijkstra_approx, 10, 10, ks=[0.1, 0.2, 0.5])
# experiment1_graph(data, 10, "Dijkstra", ks=[0.1, 0.2, 0.5])

# data = experiment1_data(f.dijkstra, a.dijkstra_approx, 20, 10)
# experiment1_graph(data, 20, "Dijkstra")
#
# data = experiment1_data(f.dijkstra, a.dijkstra_approx, 30, 10)
# experiment1_graph(data, 30, "Dijkstra")


# data = experiment1_data(f.bellman_ford, a.bellman_ford_approx, 10, 10, ks=[0.1, 0.2, 0.5])
# experiment1_graph(data, 10, "Bellman-Ford", ks=[0.1, 0.2, 0.5])

# data = experiment1_data(f.bellman_ford, a.bellman_ford_approx, 20, 10)
# experiment1_graph(data, 20, "Bellman-Ford")
#
# data = experiment1_data(f.bellman_ford, a.bellman_ford_approx, 30, 10)
# experiment1_graph(data, 30, "Bellman-Ford")

# --------------------------------------- Experiment 2 ---------------------------------------------
def experiment2_data(n, funcs, approx_funcs, func_names): #gda graph
    k_values = [1, 2, 3]
    final_list = [[], [], []]
    x_axis = []

    for i in range(len(funcs)):
        for edges in range(n, (2 * f.triangle(n - 1)) + 1):
            x_axis.append(edges)
            G = f.create_random_graph(n, edges, 1, 100)
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

# experiment2_data(20, [f.dijkstra, f.bellman_ford], [a.dijkstra_approx, a.bellman_ford_approx], ["Dijkstra", "Bellman-Ford"])

# ------------------------------- Experiment 3 -------------------------------------------
def experiment3_dijkstra(graph_size, min_edge, max_edge, max_k_value):
    total_dist = {}
    # Use this graph for all of the approximations
    G = f.create_random_complete_graph(graph_size, min_edge, max_edge)
    total_dist[0] = f.dijkstra(G, 0)

    # Calculates the approximate distance based on k value
    for i in range(max_k_value):
        total_dist[i + 1] = a.dijkstra_approx(G, 0, i + 1)

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


def experiment3_bellman(graph_size, min_edge, max_edge, max_k_value):
    total_dist = {}
    # Use this graph for all of the approximations
    G = f.create_random_complete_graph(graph_size, min_edge, max_edge)
    total_dist[0] = f.bellman_ford(G, 0)

    # Calculates the approximate distance based on k value
    for i in range(max_k_value):
        total_dist[i + 1] = a.bellman_ford_approx(G, 0, i + 1)

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


# experiment3_dijkstra(10, 1, 10, 9)
# experiment3_dijkstra(25, 1, 25, 24)
# experiment3_dijkstra(50, 1, 50, 49)

# experiment3_bellman(10, 1, 10, 9)
# experiment3_bellman(25, 1, 25, 24)
# experiment3_bellman(50, 1, 50, 49)

#-------------------------------------- Mystery Experiment ----------------------------

def experiment_mystery():
    max_node_num = 40
    trial_num = 50
    average_times = []

    for node_num in tqdm(range(1, max_node_num + 1)):
        times = []

        for _ in range(trial_num):
            G = f.create_random_complete_graph(node_num, 1, 1000)

            start_time = timeit.default_timer()
            f.mystery(G)
            end_time = timeit.default_timer()

            times.append(end_time - start_time)

        average_times.append(sum(times) / len(times))

    xs = [i for i in range(1, max_node_num + 1)]
    plot.title("Graph Size vs Runtime for Mystery Algorithm")
    plot.xlabel("log(Graph Size)")
    plot.ylabel("log(Runtime)")
    plot.loglog(xs, average_times)
    plot.show()

    plot.title("Graph Size vs Runtime for Mystery Algorithm")
    plot.xlabel("Graph Size")
    plot.ylabel("Runtime")
    plot.plot(xs, average_times)
    plot.show()

    return average_times

# experiment_mystery()
