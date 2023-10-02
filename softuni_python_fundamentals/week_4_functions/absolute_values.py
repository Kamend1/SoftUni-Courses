def absolute_value(num):
    abs_num = abs(num)
    return abs_num

numbers_input = [float(x) for x in input().split()]
numbers_abs = []

for num in numbers_input:
    numbers_abs.append(absolute_value(num))

print(numbers_abs)
