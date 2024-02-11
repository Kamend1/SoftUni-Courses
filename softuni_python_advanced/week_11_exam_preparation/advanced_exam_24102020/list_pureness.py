from collections import deque


def best_list_pureness(user_list, num):
    rotations = 0
    best_pureness = sum(value * idx for idx, value in enumerate(user_list))
    best_turn = 0
    user_list = deque(user_list)

    for _ in range(num):
        current_pureness = 0
        user_list.rotate()
        rotations += 1
        if rotations == len(user_list):
            rotations = 0

        for idx in range(len(user_list)):
            current_pureness += user_list[idx] * idx

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_turn = rotations


    return f"Best pureness {best_pureness} after {best_turn} rotations"


test = ([0, 0, 0, 0, 0], 1)
result = best_list_pureness(*test)
print(result)
