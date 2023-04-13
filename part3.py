import final_project_part1 as f1
import heuristic
import matplotlib.pyplot as plot
import csv
import min_heap
import line_info
import timeit
import heuristic_graph

def csv_graph():
    heuristic_generator = heuristic.Heuristic()
    with open('london_connections.csv') as file:
        reader = csv.DictReader(file)
        reader = list(reader)

        G = heuristic_graph.HeuristicGraph()

        for row in reader:
            if row['station1'] not in G.adj.keys():
                G.add_node(row['station1'])
            if row['station2'] not in G.adj.keys():
                G.add_node(row['station2'])
            G.add_edge(row['station1'], row['station2'], float(row['time']))

        G.set_heuristic(heuristic_generator.get_heuristic_all_pairs(G))

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
#num_lines() and num_transfers() that takes in a shortest path and returns a number

def line_transfers_all_pairs():
    stations = []
    G = csv_graph()
    with open('london_stations.csv') as rfile:
        with open('transfer_info.csv', 'w', newline ='') as wfile1:
            with open('line_info.csv', 'w', newline ='') as wfile2:
                writer1 = csv.writer(wfile1)
                writer1.writerow(['station1','station2','transfers'])
                writer2 = csv.writer(wfile2)
                writer2.writerow(['station1','station2','lines'])
                reader = csv.DictReader(rfile)
                reader = list(reader)
                for row in reader:
                    stations.append(row['id'])
                for station1 in stations:
                    for station2 in stations:
                        LI = line_info.LineInfo()
                        shortest_path = dijkstra(G, station1, station2)
                        writer1.writerow([station1, station2, LI.num_transfers(shortest_path)])
                        writer2.writerow([station1, station2, LI.num_lines(shortest_path)])

def dijkstra(G, s, d):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    shortest_path = []
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0)

    while not Q.is_empty():
        current_element = Q.extract_min()
        if current_element.value == d:
            break
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node

    # Create the shortest path
    backtrack_node = d
    while backtrack_node != s:
        shortest_path.append(backtrack_node)
        backtrack_node = pred[backtrack_node]
    shortest_path.append(s)
    shortest_path.reverse()

    return pred, shortest_path

def get_transfer_data():
    transfer_data = {}
    with open('transfer_info.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            transfer_data[(row['station1'], row['station2'])] = row['transfers']
            transfer_data[(row['station2'], row['station1'])] = row['transfers']
    return transfer_data

def experiment8():
    dijkstra_times = []
    astar_times = []
    G = csv_graph()
    transfer_data = get_transfer_data()
    count = 0
    for comb in transfer_data:
        if int(transfer_data[comb]) > 3:
            count += 1
            if (count%1000 == 0):
                print(count)
            start_time = timeit.default_timer()
            dijkstra(G, comb[0], comb[1])
            end_time = timeit.default_timer()
            dijkstra_times.append(end_time - start_time)

            start_time = timeit.default_timer()
            G.a_star_heuristic(comb[0], comb[1])
            end_time = timeit.default_timer()
            astar_times.append(end_time - start_time)
    print(sum(dijkstra_times) / len(dijkstra_times))
    print(sum(astar_times) / len(astar_times))

experiment8()

#print(csv_graph().heuristic)