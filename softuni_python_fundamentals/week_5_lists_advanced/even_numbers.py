numbers_list = [int(x) for x in input().split(',')]
even_numbers_index_list = []

for idx in range(len(numbers_list)):
    if numbers_list[idx] % 2 == 0:
        even_numbers_index_list.append(idx)

print(even_numbers_index_list)
