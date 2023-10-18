
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# ‘ункци€ обработки кнопок мыши, отключаетс€ как только пользователь введЄт координаты отрезка
def on_click(event):
    global xA, yA, xB, yB, cid

    # ќбработка левой кнопки мыши, отвечающа€ за получение координат многоугольника
    if event.button == 1:
        # image.putpixel((round(event.xdata), round(event.ydata)), (255, 0, 0))
        polygon_axes.append([round(event.xdata), round(event.ydata)])

    # ќбработка правой кнопки мыши, отвечающа€ за получение координат отрезка
    elif event.button == 3:
        # image.putpixel((round(event.xdata), round(event.ydata)), (0, 255, 0))
        # ѕолучение координат первой точки
        if(xA == yA == None):
            xA, yA = round(event.xdata), round(event.ydata)
        # ѕолучение координаты второй точки, окончание обработки событий мыши
        else:
            xB, yB = round(event.xdata), round(event.ydata)
            plt.disconnect(cid)

def Bresenham(x0, y0, x1, y1, color = (255, 255, 255)):
    delta_x = abs(x1 - x0)
    delta_y = abs(y1 - y0)
    error = 0
    diff = 1

    # —мена координат в случае, если начальна€ координата дальше по оси х, чем конечна€
    if(x0 - x1 > 0):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    # ѕроверка на убывание
    if(y0 - y1 > 0):
        diff = -1

    # ≈сли угол меньше или равно 45, то увеличиваем/уменьшаем координату y
    if(delta_x >= delta_y):
        y_i = y0
        for x in range(x0, x1 + 1):
            image.putpixel((x, y_i), color)
            error = error + 2 * delta_y
            if error >= delta_x:
                y_i += diff
                error -= 2 * delta_x
    # »наче - по координате x
    elif(delta_x < delta_y):
        # ќбработка особого случа€
        if(diff == -1):
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        x_i = x0
        for y in range(y0, y1 + 1):
            image.putpixel((x_i, y), color)
            error = error + 2 * delta_x
            if error >= delta_y:
                x_i += diff
                error -= 2 * delta_y

def Cyrus_Beck():
    global xA, yA, xB, yB, polygon_axes

    tA, tB = 0, 1
    Dx, Dy = (xB - xA), (yB - yA)

    for i in range(-1, len(polygon_axes)-1):
        xp1, yp1 = int(polygon_axes[i][0]), int(polygon_axes[i][1])
        xp2, yp2 = int(polygon_axes[i+1][0]), int(polygon_axes[i+1][1])

        #  оординаты внутренней нормали
        xN, yN = yp1 - yp2, xp2 - xp1

       
        Qi = (xA - xp1)*xN + (yA - yp1)*yN

        # —кал€рное произведение дл€ определени€ ориентации отрезка относительно i-й стороны окна
        Pi = Dx*xN + Dy*yN

        # ¬ырождение: или точка, или отрезок вне окна
        if(Pi == 0):
            # ќтрезок вне окна, отсечение закончено
            # »наче рассматриваем след. отрезок
            if(Qi < 0): return None, None
            continue
        
        t = - (Qi / Pi)
        if not(0 <= t <= 1): continue

        if(Pi < 0):
            tA = max(tA, t)
        else:
            tB = min(tB, t)

    if (tA <= tB):
        return tA, tB
    
    return None, None

polygon_axes = []
xA, yA, xB, yB = None, None, None, None
image = Image.new('RGB', (30, 30))
image = ImageOps.flip(image)
cid = plt.connect("button_press_event", on_click)

# «аполнение координатной плоскости серыми квадратами дл€ лучшего визуального наблюдени€
for x in range(0, image.width):
    for y in range(0, image.height):
        if(x%2 == y%2):
            image.putpixel((x, y), (54, 54, 54))

plt.imshow(image)
plt.show()

# ѕрорисовка изначального положени€ пр€мой
Bresenham(xA, yA, xB, yB, (255, 0, 0))

# ѕрорисовка многоугольника
for i in range(-1, len(polygon_axes)-1):
    Bresenham(polygon_axes[i][0], polygon_axes[i][1], polygon_axes[i+1][0], polygon_axes[i+1][1], (0, 0, 255))

# ѕолучаем параметры начала и конца отсечЄнного отрезка в виде параметров точек
t_begin, t_end = Cyrus_Beck()

# ≈сли выполн€етс€ условие, то отрисовываем линию, получив координаты точек через параметрическое уравнение,
# с поправкой на то, что часть отрезка или весь отрезок может оказатьс€ внутри
if ((t_begin and t_end) != None):
    if(t_begin != 0):
        xA, yA = round(xB*t_begin + xA*(1-t_begin)), round(yB*t_begin + yA*(1-t_begin))
    if(t_end != 1):
        xB, yB = round(xB*t_end + xA*(1-t_end)), round(yB*t_end + yA*(1-t_end))

    Bresenham(xA, yA, xB, yB)

plt.imshow(image)
plt.show()

print("OK!")