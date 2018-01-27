import math
import sys
from tsp_file_util import *


def calc_tour_length(tsp_file_path, tour_file_path):
    tsp = read_tsp_file(tsp_file_path)
    tour = read_tour_file(tour_file_path)

    prev = tour[len(tour) - 1]

    length = 0
    for city in tour:
        dx = tsp[prev][0] - tsp[city][0]
        dy = tsp[prev][1] - tsp[city][1]
        length += int(math.sqrt(dx * dx + dy * dy) + 0.5)
        prev = city
    print(length)


if __name__ == "__main__":
    calc_tour_length(sys.argv[1], sys.argv[2])
