from collections import deque
def fill_the_box(length, width, height, *args):
    volume = length * width * height
    cubes = deque(args)
    while cubes:
        current_cubes = cubes.popleft()
        if current_cubes == 'Finish':
            return f"There is free space in the box. You could put {volume} more cubes."
            break
        if current_cubes > volume:
            cubes.pop()
            current_cubes -= volume
            cubes.appendleft(current_cubes)
            cubes_left = sum(cubes)
            return f"No more free space! You have {cubes_left} more cubes."
            break
        else:
            volume -= current_cubes

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))