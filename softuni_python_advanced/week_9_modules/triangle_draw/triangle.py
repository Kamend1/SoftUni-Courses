def draw_upper_part(n):
    result = ""
    for i in range(1, n + 1):
        print(*range(1, i + 1))


def draw_lower_part(n):
    for i in range(n, 0, -1):
        print(*range(1, i))


def draw_triangle(n):
    draw_upper_part(n)
    draw_lower_part(n)
