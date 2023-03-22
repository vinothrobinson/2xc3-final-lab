import min_heap
import final_project_part1
import part1
import timeit

def experiment1_data(func, func_approx, node_num, trial_num, lower_bound = 1):
    avg_times = [[] for i in range(4)]

    for edge_num in range(node_num, 2 * final_project_part1.triangle(node_num-1) + 1):
        times = [0 for _ in range(4)]
        for _ in range(trial_num):
            G = final_project_part1.create_random_graph(node_num, edge_num, lower_bound, 1000)

            start_time = timeit.default_timer()
            func(G, 0)
            end_time = timeit.default_timer()

            times[0] += end_time - start_time

            for i, k in enumerate([0.25, 0.5, 0.75]):
                start_time = timeit.default_timer()
                func_approx(G, 0, k * node_num)
                end_time = timeit.default_timer()

                times[i+1] += end_time - start_time

        for i in range(4):
            avg_times[i].append(times[i] / trial_num)

    return avg_times


Ls = experiment1_data(final_project_part1.dijkstra, part1.dijkstra_approx, 25, 100)
print(Ls)