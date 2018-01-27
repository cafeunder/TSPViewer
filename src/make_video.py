import os
import sys
from tsp_file_util import *
from PIL import Image, ImageDraw, ImageFont


def tour_plot_pil(tsp_file_name, tour_file_name, number, index, length):
    tsp = read_tsp_file(tsp_file_name)
    tour = read_tour_file(tour_file_name)
    base, _ = os.path.splitext(tour_file_name)

    tour_coord_x = []
    tour_coord_y = []
    for city in tour:
        tour_coord_x.append(tsp[city][0])
        tour_coord_y.append(tsp[city][1])

    canvas = Image.new('RGB', (756, 1024), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    s = 1.95
    prev = tour[len(tour) - 1]
    for city in tour:
        draw.line((tsp[prev][0] / s, tsp[prev][1] / s, tsp[city][0] / s, tsp[city][1] / s), fill=(10, 10, 10))
        prev = city

    font = ImageFont.truetype("/usr/share/fonts/truetype/lato/Lato-Medium.ttf", 32)
    draw.text((420, 835), "2-Opt: " + str(number), fill="#000", font=font)
    draw.text((420, 875), "length: " + str(length), fill="#000", font=font)

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
        tour_plot_pil(tsp_file_path, tour_dir_path + "/" + str(number) + ".tour", number, index, 0)
        index += 1


if __name__ == "__main__":
    make_video(sys.argv[1], sys.argv[2])
    os.system('ffmpeg -framerate 40 -i png/%d.png -vcodec libx264 -pix_fmt yuv420p -r 40 out.mp4')
    os.system('rm png/*')

