import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def draw_circle_bresenham(center_x, center_y, radius):
    # ������� ������ �����������
    width = radius * 2
    height = radius * 2
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    x = 0
    y = radius
    d = 3 - 2 * radius

    def plot_circle_points(x, y):
        draw.point((center_x + x, center_y + y), fill="black")
        draw.point((center_x - x, center_y + y), fill="black")
        draw.point((center_x + x, center_y - y), fill="black")
        draw.point((center_x - x, center_y - y), fill="black")
        draw.point((center_x + y, center_y + x), fill="black")
        draw.point((center_x - y, center_y + x), fill="black")
        draw.point((center_x + y, center_y - x), fill="black")
        draw.point((center_x - y, center_y - x), fill="black")

    while x <= y:
        plot_circle_points(x, y)
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

    image.show()

# ������ �������������:
center_x = 100  # ���������� ������ ����������
center_y = 100
radius = 50     # ������ ����������
draw_circle_bresenham(center_x, center_y, radius)

