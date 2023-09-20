def draw_figure(n):
    stars = 1
    for i in range(n):
        print('*' * i)
        stars -= 1

    for i in range(n, 0, -1):
        print('*' * i)
        stars += 1

n = int(input())
draw_figure(n)
