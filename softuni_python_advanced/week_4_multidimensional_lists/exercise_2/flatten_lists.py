input_list = [x.split() for x in input().split('|')]
flattened_list = []

for list in input_list[::-1]:
    for element in list:
        flattened_list.append(element)

print(' '.join(flattened_list))
