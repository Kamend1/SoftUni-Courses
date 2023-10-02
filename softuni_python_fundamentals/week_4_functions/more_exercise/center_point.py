from math import sqrt, floor

def distance_to_center_point(x1, y1, x2, y2):
    distance_1 = sqrt(x1 ** 2 + y1 ** 2)
    distance_2 = sqrt(x2 ** 2 + y2 ** 2)

    if distance_1 <= distance_2:
        print(f"({floor(x1):.0f}, {floor(y1):.0f})")
    elif distance_1 > distance_2:
        print(f"({floor(x2):.0f}, {floor(y2):.0f})")

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

distance_to_center_point(x1, y1, x2, y2)
