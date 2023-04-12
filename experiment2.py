import csv
import timeit

import karl


def experiment5(subway, transfer_data):
    for line1 in subway.adj.keys():
        for line2 in subway.adj.keys():
            if transfer_data[(line1, line2)] == 0:
                start = timeit.default_timer()


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
experiment5(subway_graph, transfer_data)
