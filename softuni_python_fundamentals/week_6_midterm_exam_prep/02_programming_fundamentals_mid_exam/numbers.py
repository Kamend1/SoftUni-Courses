sequence = [int(x) for x in input().split()]
above_average_list = []
list_to_print = []
average = sum(sequence) / len(sequence)

for idx in range(len(sequence)):
    if sequence[idx] > average:
        above_average_list.append(sequence[idx])

above_average_list.sort(reverse=True)
if len(above_average_list) >= 5:
    list_to_print = above_average_list[:5]
else:
    list_to_print = above_average_list

if len(list_to_print) == 0:
    print("No")
else:
    print(*list_to_print, sep=" ")
