import os
import sys
import numpy as np
from calc_tour_length import calc_tour_length
from tsp_file_util import *
from PIL import Image, ImageDraw, ImageFont


def tour_plot_pil(tsp_file_name, tour_file_name, number, index):
    SCREEN_WIDTH = 756
    SCREEN_HEIGHT = 1024
    MARGIN = 20
    TSP_WIDTH = SCREEN_WIDTH - (MARGIN * 2)
    TSP_HEIGHT = SCREEN_HEIGHT - (MARGIN * 2)

    tsp = np.array(read_tsp_file(tsp_file_name))
    tour = read_tour_file(tour_file_name)
    base, _ = os.path.splitext(tour_file_name)

    xmin = tsp[:, :1].min()
    ymin = tsp[:, 1:].min()

    tsp[:, :1] -= xmin
    tsp[:, 1:] -= ymin
    xmax = tsp[:, :1].max()
    ymax = tsp[:, 1:].max()

    if TSP_HEIGHT / TSP_WIDTH < ymax / xmax:
        tsp[:, :1] = tsp[:, :1] / ymax * TSP_HEIGHT
        tsp[:, 1:] = tsp[:, 1:] / ymax * TSP_HEIGHT
    else:
        tsp[:, :1] = tsp[:, :1] / xmax * TSP_WIDTH
        tsp[:, 1:] = tsp[:, 1:] / xmax * TSP_WIDTH

    tsp[:, :1] += MARGIN
    tsp[:, 1:] += MARGIN

    canvas = Image.new('RGB', (SCREEN_WIDTH, SCREEN_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    count = 0
    s = 1
    prev = tour[len(tour) - 1]
    # 17000
    for city in tour:
        draw.line((tsp[prev][0] / s, tsp[prev][1] / s, tsp[city][0] / s, tsp[city][1] / s), fill=(10, 10, 10))
        prev = city

    font = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Medium.ttf", 32)
    # font = ImageFont.truetype("calibri.ttf", 32)
    draw.text((100, 835), "2-Opt: " + str(number), fill="#000", font=font)
    draw.text((100, 875), "length: " + str(calc_tour_length(tsp_file_name, tour_file_name)), fill="#000", font=font)

    if not os.path.exists("png"):
        os.mkdir("png")
    canvas.save("png/" + str(index + 1) + ".png", "PNG")


def make_video(tsp_file_path, tour_dir_path):
    number_list = []
    for file in os.listdir(tour_dir_path):
        base, ext = os.path.splitext(file)
        if ext == ".tour":
            number_list.append(int(base))

    index = 0
    number_list.sort()
    for number in number_list:
        print(tour_dir_path + "/" + str(number) + ".tour")
        tour_plot_pil(tsp_file_path, tour_dir_path + "/" + str(number) + ".tour", number, index)
        index += 1


if __name__ == "__main__":
    make_video(sys.argv[1], sys.argv[2])
    os.system('ffmpeg -framerate 40 -i png/%d.png -vcodec libx264 -pix_fmt yuv420p -r 40 out.mp4 -y')
    os.system('rm png/*')
