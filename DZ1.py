import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def draw_bresenham_line(x1, y1, x2, y2):
    if not all(isinstance(coord, int) for coord in [x1, y1, x2, y2]):
        print("The entered coordinates are incorrect. Use only integers.")
        return

    img = Image.new('RGB', (abs(x2 - x1) + 1, abs(y2 - y1) + 1), color='white')
    draw = ImageDraw.Draw(img)

   
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy  

    x, y = x1, y1

    while True:
        draw.point((x - x1, y - y1), fill='black')

        if x == x2 and y == y2:
            break

        e2 = 2 * err

        if e2 > -dy: 
            err -= dy
            x += sx

        if e2 < dx:
            err += dx
            y += sy

    img.show()


x1, y1 = 10, 10
x2, y2 = 100, 50
draw_bresenham_line(x1, y1, x2, y2)


