from math import pi

shape_of_figure = str(input())
area = 0

if shape_of_figure == "square":
    side = float(input())
    area = side * side
elif shape_of_figure == "rectangle":
    width = float(input())
    length = float(input())
    area = width * length
elif shape_of_figure == "circle":
    radius = float(input())
    area = pi * radius * radius
elif shape_of_figure == "triangle":
    side_triangle = float(input())
    height_triangle = float(input())
    area = (side_triangle * height_triangle) / 2

print(f"{area:.3f}")
