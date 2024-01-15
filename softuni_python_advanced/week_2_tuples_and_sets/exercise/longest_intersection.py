counter = int(input())
raw_data = []
longest_intersection = []
max_length = 0

for _ in range(counter):
    raw_data.append(input())

for data in raw_data:
    set_1 = set()
    set_2 = set()
    first_start, mid_range, second_end = data.split(',')
    first_end, second_start = mid_range.split('-')
    for i in range(int(first_start), int(first_end) + 1):
        set_1.add(i)
    for j in range(int(second_start), int(second_end) + 1):
        set_2.add(j)
    current_intersection = set_1.intersection(set_2)
    if len(current_intersection) > len(longest_intersection):
        max_length = len(current_intersection)
        longest_intersection = list(current_intersection)

print(f"Longest intersection is {longest_intersection} with length {max_length}")
