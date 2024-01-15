counter = int(input())
raw_data = []
longest_intersection = []
max_length = 0

for _ in range(counter):
    raw_data.append(input())

for data in raw_data:
    first_start, mid_range, second_end = data.split(',')
    first_end, second_start = mid_range.split('-')

    set_1 = set(range(int(first_start), int(first_end) + 1))
    set_2 = set(range(int(second_start), int(second_end) + 1))
    current_intersection = set_1.intersection(set_2)

    if len(current_intersection) > len(longest_intersection):
        max_length = len(current_intersection)
        longest_intersection = list(current_intersection)

print(f"Longest intersection is {longest_intersection} with length {max_length}")
