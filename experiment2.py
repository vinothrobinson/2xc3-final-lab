import csv
import timeit
import tqdm
import karl


def experiment5(subway, transfer_data):
    dijkstra_times = []
    a_star_times = []

    for i, line1 in enumerate(subway.adj.keys()):
        print(f"iteration {i}")
        for line2 in subway.adj.keys():
            if transfer_data[(line1, line2)] == '0':
                start = timeit.default_timer()
                karl.dijkstra(subway, line1, line2)
                end = timeit.default_timer()
                dijkstra_times.append(end - start)

                start = timeit.default_timer()
                subway.a_star_heuristic(line1, line2)
                end = timeit.default_timer()
                a_star_times.append(end - start)

    return sum(dijkstra_times) / len(dijkstra_times), sum(a_star_times) / len(a_star_times)


def get_transfer_data():
    transfer_data = {}
    with open('karl1.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            transfer_data[(row['station1'], row['station2'])] = row['transfers']
            transfer_data[(row['station2'], row['station1'])] = row['transfers']
    return transfer_data


subway_graph = karl.csv_graph()
transfer_data = get_transfer_data()
times = experiment5(subway_graph, transfer_data)

print(f"Dijkstra: {times[0]}")
print(f"A*: {times[1]}")