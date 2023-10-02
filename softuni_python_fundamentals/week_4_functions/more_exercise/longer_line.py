from math import sqrt, floor


def distance_to_center_point(x1, y1, x2, y2):
    result = ""
    distance_1 = sqrt(x1 ** 2 + y1 ** 2)
    distance_2 = sqrt(x2 ** 2 + y2 ** 2)

    if distance_1 <= distance_2:
        result = "point_1"
    elif distance_1 > distance_2:
        result = "point_2"
    return result


def longer_line_between_points(x1, y1, x2, y2, x3, y3, x4, y4):
    result = ""
    distance_1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    distance_2 = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)

    if distance_1 >= distance_2 and distance_to_center_point(x1, y1, x2, y2) == "point_1":
        result = (f"({floor(x1):.0f}, {floor(y1):.0f})({floor(x2):.0f}, {floor(y2):.0f})")
    elif distance_1 >= distance_2 and distance_to_center_point(x1, y1, x2, y2) == "point_2":
        result = (f"({floor(x2):.0f}, {floor(y2):.0f})({floor(x1):.0f}, {floor(y1):.0f})")
    elif distance_1 < distance_2 and distance_to_center_point(x3, y3, x4, y4) == "point_1":
        result = (f"({floor(x3):.0f}, {floor(y3):.0f})({floor(x4):.0f}, {floor(y4):.0f})")
    elif distance_1 < distance_2 and distance_to_center_point(x3, y3, x4, y4) == "point_2":
        result = (f"({floor(x4):.0f}, {floor(y4):.0f})({floor(x3):.0f}, {floor(y3):.0f})")
    return result

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line_between_points(x1, y1, x2, y2, x3, y3, x4, y4))
