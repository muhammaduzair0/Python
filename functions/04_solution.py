import math

def circle_stats(radius):
    area = math.floor(math.pi * radius ** 2)
    circumference = math.floor(2 * math.pi * radius)
    return area, circumference

a, c = circle_stats(3)


print("Area: ", a, "Circumference: ", c)