from collections import deque
def fill_the_box(*args):
    arguments = deque(args)
    length = arguments.popleft()
    width = arguments.popleft()
    height = arguments.popleft()
    volume = length * width * height

    while arguments:
        current_cubes = arguments.popleft()
        if current_cubes == 'Finish':
            return f"There is free space in the box. You could put {volume} more cubes."
            break
        if current_cubes > volume:
            arguments.pop()
            current_cubes -= volume
            arguments.appendleft(current_cubes)
            cubes_left = sum(arguments)
            return f"No more free space! You have {cubes_left} more cubes."
            break
        else:
            volume -= current_cubes

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))