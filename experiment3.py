import csv
import random
import timeit

import a_star
import karl
import refactor


def get_transfer_data():
    transfer_data = {}
    with open('karl1.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            transfer_data[(row['station1'], row['station2'])] = row['transfers']
            transfer_data[(row['station2'], row['station1'])] = row['transfers']
    return transfer_data


def experiment5(subway):
    dijkstra_times = []
    a_star_times = []

    for i, line1 in enumerate(subway.adj.keys()):
        if i > 8:
            break
        print(f"iteration {i}")

        for line2 in subway.adj.keys():
            start = timeit.default_timer()
            karl.dijkstra(subway, line1, line2)
            end = timeit.default_timer()
            dijkstra_times.append(end - start)

            h = lambda n: subway.get_heuristic()[(n, line2)]
            start = timeit.default_timer()
            a_star.a_star(subway, line1, line2, h)
            end = timeit.default_timer()
            a_star_times.append(end - start)

    return sum(dijkstra_times) / len(dijkstra_times), sum(a_star_times) / len(a_star_times)


def experiment6(subway, transfer_data):
    dijkstra_times = []
    a_star_times = []

    for i, line1 in enumerate(subway.adj.keys()):
        if i > 8:
            break
        print(f"iteration {i}")

        for line2 in subway.adj.keys():
            if transfer_data[(line1, line2)] == '0':
                start = timeit.default_timer()
                karl.dijkstra(subway, line1, line2)
                end = timeit.default_timer()
                dijkstra_times.append(end - start)

                h = lambda n: subway.get_heuristic()[(n, line2)]
                start = timeit.default_timer()
                a_star.a_star(subway, line1, line2, h)
                end = timeit.default_timer()
                a_star_times.append(end - start)

    return sum(dijkstra_times) / len(dijkstra_times), sum(a_star_times) / len(a_star_times)


def experiment7(subway, transfer_data):
    dijkstra_times = []
    a_star_times = []

    for i, line1 in enumerate(subway.adj.keys()):
        if i > 8:
            break
        print(f"iteration {i}")

        for line2 in subway.adj.keys():
            if transfer_data[(line1, line2)] == '1':
                start = timeit.default_timer()
                karl.dijkstra(subway, line1, line2)
                end = timeit.default_timer()
                dijkstra_times.append(end - start)

                h = lambda n: subway.get_heuristic()[(n, line2)]
                start = timeit.default_timer()
                a_star.a_star(subway, line1, line2, h)
                end = timeit.default_timer()
                a_star_times.append(end - start)

    return sum(dijkstra_times) / len(dijkstra_times), sum(a_star_times) / len(a_star_times)


def experiment8(subway, transfer_data):
    dijkstra_times = []
    a_star_times = []

    for i, line1 in enumerate(subway.adj.keys()):
        if i > 8:
            break
        print(f"iteration {i}")

        for line2 in subway.adj.keys():
            if int(transfer_data[(line1, line2)]) > 1:
                start = timeit.default_timer()
                karl.dijkstra(subway, line1, line2)
                end = timeit.default_timer()
                dijkstra_times.append(end - start)

                h = lambda n: subway.get_heuristic()[(n, line2)]
                start = timeit.default_timer()
                a_star.a_star(subway, line1, line2, h)
                end = timeit.default_timer()
                a_star_times.append(end - start)

    return sum(dijkstra_times) / len(dijkstra_times), sum(a_star_times) / len(a_star_times)


def experiment_neg2():
    def dict_equal(d1, d2):
        for key in d1.keys():
            if key not in d2.keys():
                return False
            if d1[key] != d2[key]:
                return False
        return True

    subway_graph = karl.csv_graph()
    d = {
        ("slower", "different") : 0,
        ("slower", "same") : 0,
        ("faster", "different") : 0,
        ("faster", "same") : 0
    }
    for _ in range(1000):
        n1 = str(random.choice(list(subway_graph.adj.keys())))
        n2 = str(random.choice(list(subway_graph.adj.keys())))

        start = timeit.default_timer()
        p1 = karl.dijkstra(subway_graph, n1, n2)[0]
        end = timeit.default_timer()
        t1 = end - start

        start = timeit.default_timer()
        p2 = subway_graph.a_star_heuristic(n1, n2)[0]
        end = timeit.default_timer()
        t2 = end - start

        if t2 < t1:
            if dict_equal(p1, p2):
                d[("faster", "same")] += 1
            else:
                d[("faster", "different")] += 1
        else:
            if dict_equal(p1, p2):
                d[("slower", "same")] += 1
            else:
                d[("slower", "different")] += 1

    for key in d.keys():
        print(f"{key} : {d[key]}")


# subway_graph = karl.csv_graph()
# transfer_data = get_transfer_data()
# times = experiment6(subway_graph, transfer_data)
# print(f"Dijkstra: {times[0]}")
# print(f"A*: {times[1]}")

def experiment_neg3():

    subway_graph = karl.csv_graph()
    d = {
        "slower" : ([], []),
        "faster" : ([], []),
    }
    for _ in range(10000):
        n1 = str(random.choice(list(subway_graph.adj.keys())))
        n2 = str(random.choice(list(subway_graph.adj.keys())))

        if n1 == n2:
            continue

        start = timeit.default_timer()
        l1 = refactor.Dijkstra.calc_sp(subway_graph, n1, n2)
        end = timeit.default_timer()
        t1 = end - start

        start = timeit.default_timer()
        l2 = refactor.A_Star_Adapter.calc_sp(subway_graph, n1, n2, lambda n: subway_graph.get_heuristic()[(n, n2)])
        end = timeit.default_timer()
        t2 = end - start

        if t2 < t1:
            d["slower"][0].append(subway_graph.get_heuristic()[(n1, n2)])
            d["slower"][1].append(l1)
        else:
            d["faster"][0].append(subway_graph.get_heuristic()[(n1, n2)])
            d["faster"][1].append(l1)

    for key in d.keys():
        print(f"{key}:")
        print(f"\ttotal: {len(d[key][0])}")
        print(f"\tavg heuristic: {sum(d[key][0]) / len(d[key][0])}")
        print(f"\tmin heuristic: {min(d[key][0])}")
        print(f"\tmax heuristic: {max(d[key][0])}")

        print(f"\tavg path length: {sum(d[key][1]) / len(d[key][1])}")
        print(f"\tmin path length: {min(d[key][1])}")
        print(f"\tmax path length: {max(d[key][1])}")


experiment_neg3()