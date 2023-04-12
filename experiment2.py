import csv

import karl


def experiment5(subway, transfer_data):
    pass

subway_graph = karl.csv_graph()
transfer_data = {}
with open('karl1.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        transfer_data[(row['station1'], row['station2'])] = row['trasfers']
        transfer_data[(row['station2'], row['station1'])] = row['transfers']

experiment5(subway_graph, transfer_data)