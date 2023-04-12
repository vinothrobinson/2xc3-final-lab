import csv


class LineInfo:
    edge_lines = {}

    def __init__(self):
        with open('london_connections.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self.edge_lines[(row['station1'], row['station2'])] = row['line']
                self.edge_lines[(row['station2'], row['station1'])] = row['line']

    def num_lines(self, path):
        lines = set()

        for i in range(0, len(path) - 1):
            lines.add(self.edge_lines[path[i], path[i + 1]])

        return len(lines)

    def num_transfers(self, path):
        transfers = 0

        current_line = self.edge_lines[path[0], path[1]]
        for i in range(1, len(path) - 1):
            next_line = self.edge_lines[path[i], path[i + 1]]
            if next_line != current_line:
                transfers += 1
                current_line = next_line

        return transfers