def read_points_from_file(filename):
    with open(filename, "r") as file:
        matrix = [[float(num) for num in line.split(',')] for line in file]

        return matrix


def read_connections_from_file(filename):
    with open(filename, "r") as file:
        connections = [[int(num) for num in line.split(',')] for line in file]

        return connections
