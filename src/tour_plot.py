import os
import sys
import matplotlib.pyplot as plt
from tsp_file_util import *


def tour_plot(tsp_file_name, tour_file_name, output):
    tsp = read_tsp_file(tsp_file_name)
    tour = read_tour_file(tour_file_name)
    base, _ = os.path.splitext(tour_file_name)

    tour_coord_x = []
    tour_coord_y = []
    for city in tour:
        tour_coord_x.append(tsp[city][0])
        tour_coord_y.append(tsp[city][1])

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    plt.plot(tour_coord_x, tour_coord_y, linewidth=.1, color="#000000")
    plt.xlim(min(tour_coord_x), max(tour_coord_x))
    plt.ylim(max(tour_coord_y), min(tour_coord_y))

    plt.tick_params(top='off', bottom='off', labelbottom="off")
    plt.tick_params(left='off', right='off', labelleft="off")

    ax.spines["right"].set_color("None")
    ax.spines["top"].set_color("None")
    ax.spines["left"].set_color("None")
    ax.spines["bottom"].set_color("None")

    if output:
        # plt.savefig("output.pdf", bbox_inches="tight", pad_inches=0.0)
        print(base)
        plt.savefig(base + ".png", bbox_inches="tight", pad_inches=0.0, dpi=400)
    plt.show()

    plt.close()


if __name__ == "__main__":
    tour_plot(sys.argv[1], sys.argv[2], (len(sys.argv) > 3 and sys.argv[3] == "-o"))
