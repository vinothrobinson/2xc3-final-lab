import csv
import math


class Heuristic:
    stations = {}

    def __init__(self):
        with open('london_stations.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.stations[row['id']] = {'latitude': float(row['latitude']), 'longitude': float(row['longitude'])}
            print(self.stations)

    def distance(self, s1, s2):
        la1 = self.stations[s1]['latitude']
        la2 = self.stations[s2]['latitude']
        lo1 = self.stations[s1]['longitude']
        lo2 = self.stations[s2]['longitude']
        return math.sqrt(math.pow((la1 - la2), 2) + math.pow((lo1 - lo2), 2))

    def generate_heuristic(self, G, dest):
        h = {}
        for node in G.adj:
            h[node] = self.distance(node, dest)
        return h


heuristic = Heuristic()
print(heuristic.distance('2', '4'))