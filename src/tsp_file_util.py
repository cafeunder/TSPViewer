import re


def read_tsp_file(filename):
    f = open(filename, "r")
    cities = []
    read_coord = False
    for line in f:
        line = line.rstrip("\n").rstrip("\r")
        if line == "EOF":
            break

        if read_coord:
            record = re.split(" +", line)
            cities.append([float(record[1]), float(record[2])])

        if line == "NODE_COORD_SECTION":
            read_coord = True

    return cities


def read_tour_file(filename):
    f = open(filename, "r")
    tour = []
    read_city = False
    for line in f:
        line = line.rstrip("\n").rstrip("\r")
        if line == "-1":
            break

        if read_city:
            tour.append(int(line) - 1)

        if line == "TOUR_SECTION":
            read_city = True

    return tour
