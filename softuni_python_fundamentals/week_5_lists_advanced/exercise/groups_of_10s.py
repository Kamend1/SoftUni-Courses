numbers = [int(x) for x in input().split(', ')]
max_number = max(numbers)
if max_number % 10 == 0:
    number_of_groups = max_number // 10
else:
    number_of_groups = (max_number // 10) + 1
groups = []
group_numbers = []

for i in range(number_of_groups):
    groups.append([])
    group_numbers.append(str(i + 1) + '0' )

for group_idx in range(len(group_numbers)):
    for idx in range(len(numbers)):
        if group_idx == 0:
            if numbers[idx] <= int(group_numbers[group_idx]):
                groups[group_idx].append(numbers[idx])
        else:
            if int(group_numbers[group_idx - 1]) < numbers[idx] <= int(group_numbers[group_idx]):
                groups[group_idx].append(numbers[idx])
for index in range(len(groups)):
    print(f"Group of {group_numbers[index]}'s: {groups[index]}")
