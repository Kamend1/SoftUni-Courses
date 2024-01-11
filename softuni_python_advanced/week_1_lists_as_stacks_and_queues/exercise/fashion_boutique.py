clothes_value_stack = [int(x) for x in input().split()]
rack_value = int(input())

number_racks = 1
sum_current_rack = 0

while clothes_value_stack:
    if clothes_value_stack[-1] + sum_current_rack <= rack_value:
        sum_current_rack += clothes_value_stack.pop()
    else:
        number_racks += 1
        sum_current_rack = 0

print(number_racks)
