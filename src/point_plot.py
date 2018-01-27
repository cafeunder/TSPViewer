import os
import sys
import matplotlib.pyplot as plt
from tsp_file_util import *


def point_plot(tsp_file_name, output):
    tsp = read_tsp_file(tsp_file_name)
    base, _ = os.path.splitext(tsp_file_name)

    tour_coord_x = []
    tour_coord_y = []
    for city in tsp:
        tour_coord_x.append(city[0])
        tour_coord_y.append(city[1])

    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')

    plt.plot(tour_coord_x, tour_coord_y, marker=",", markersize=.1, linewidth=0, color="#000000")
    plt.xlim(min(tour_coord_x), max(tour_coord_x))
    plt.ylim(max(tour_coord_y), min(tour_coord_y))

    plt.tick_params(top='off', bottom='off', labelbottom="off")
    plt.tick_params(left='off', right='off', labelleft="off")

    ax.spines["right"].set_color("None")
    ax.spines["top"].set_color("None")
    ax.spines["left"].set_color("None")
    ax.spines["bottom"].set_color("None")

    if output:
        plt.savefig(base + ".png", bbox_inches="tight", pad_inches=0.0, dpi=300)
        # plt.savefig("output.pdf", bbox_inches="tight", pad_inches=0.0)
    plt.show()

    plt.close()


if __name__ == "__main__":
    point_plot(sys.argv[1], (len(sys.argv) > 2 and sys.argv[2] == "-o"))
