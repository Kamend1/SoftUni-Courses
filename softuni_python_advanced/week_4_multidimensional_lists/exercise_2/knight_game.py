from collections import deque


def find_all_knights(matrix, length):
    queue = []
    for row_idx in range(length):
        for col_idx in range(length):
            if matrix[row_idx][col_idx] == 'K':
                queue.append((row_idx, col_idx))
    queue.reverse()
    return queue


size = int(input())
field = [[char for char in input()] for _ in range(size)]
original_knights = len(find_all_knights(field, size))
removed_knights = 0
# attacked_fields = [(-2, -1), (-2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2), (+2, -1), (+2, +1)]
pos_nums = [-2, -1, 1, 2]
attacked_fields = [(x, y) for x in pos_nums for y in pos_nums if abs(x) != abs(y)]

while True:
    knight_coordinates = find_all_knights(field, size)
    knight_number_attacks = {}

    for _ in range(len(knight_coordinates)):
        knight = knight_coordinates.pop()
        knight_row, knight_col = knight
        for element in attacked_fields:
            added_row, added_col = element
            knight_row += added_row
            knight_col += added_col
            if 0 <= knight_row < size and 0 <= knight_col < size and field[knight_row][knight_col] == 'K':
                if knight not in knight_number_attacks:
                    knight_number_attacks[knight] = []
                knight_number_attacks[knight].append((knight_row, knight_col))
            knight_row -= added_row
            knight_col -= added_col

    sorted_attacks = deque(sorted(knight_number_attacks.items(), key=lambda x: len(x[1]), reverse=True))

    if original_knights == 1:
        break
    if sorted_attacks:
        current_knight = sorted_attacks.popleft()
        field[current_knight[0][0]][current_knight[0][1]] = '0'
        original_knights -= 1
        removed_knights += 1
    else:
        break

print(removed_knights)
