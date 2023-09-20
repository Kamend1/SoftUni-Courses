def draw_figure(n, counter):
    if n == 0:
        return

    counter += 1
    print('*' * counter)

    draw_figure(n - 1, counter)

    counter -= 1
    print('*' * counter)


n = int(input())
counter = 0
draw_figure(n, counter)
