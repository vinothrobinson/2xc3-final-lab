import final_project_part1 as f1
import part1 as f2
import matplotlib.pyplot as plot
import math
import csv

def experiment1_gda(n, funcs, approx_funcs, func_names):
    k_values = [1, 2, 3]
    final_list = [[], [], []]
    x_axis = []

    for i in range(len(funcs)):
        for edges in range(n, (2 * f1.triangle(n - 1)) + 1):
            x_axis.append(edges)
            G = f1.create_random_graph(n, edges, 1, 100)
            shortest_paths = funcs[i](G, 0)
            shortest_path = sum(shortest_paths.values())
            for index in range(len(k_values)):
                approx_paths = approx_funcs[i](G, 0, k_values[index])
                approx_path = sum(approx_paths.values())
                final_list[index].append(shortest_path / approx_path * 100)

        for index in range(len(k_values)):
            plot.plot(x_axis, final_list[index], label="k = " + str(k_values[index]))
        plot.xlabel("Graph density (measured in number of edges)")
        plot.ylabel("Accuracy of approximation")
        plot.title("Ice Spikes Biome: " + func_names[i])
        plot.legend()
        plot.show()
        plot.close()

        final_list = [[], [], []]
        x_axis = []

#experiment1_gda(20, [f1.dijkstra, f1.bellman_ford], [f2.dijkstra_approx, f2.bellman_ford_approx], ["Dijkstra", "Bellman-Ford"])


def csv_graph():
    with open('london_connections.csv') as file:
        reader = csv.DictReader(file)
        reader = list(reader)

        G = f1.DirectedWeightedGraph()

        for row in reader:
            if row['station1'] not in G.adj.keys():
                G.add_node(row['station1'])
            if row['station2'] not in G.adj.keys():
                G.add_node(row['station2'])
            G.add_edge(row['station1'], row['station2'], row['time'])

        return G

def station_list():
    with open('london_connections.csv') as file:
        reader = csv.DictReader(file)
        reader = list(reader)

        list_dict = {}

        for row in reader:
            if row['station1'] not in list_dict.keys():
                list_dict[row['station1']] = set()
            list_dict[row['station1']].add(row['line'])
            if row['station2'] not in list_dict.keys():
                list_dict[row['station2']] = set()
            list_dict[row['station2']].add(row['line'])

        return list_dict

#print(csv_graph().adj)
#print(station_list())