def sum_numbers(a, b):
    add_num = a + b
    return add_num

def subtract_numbers(c, d):
    subtract_num = c - d
    return subtract_num

def add_and_subtract(a, b, c):
    sum_number = sum_numbers(a, b)
    final_result = subtract_numbers(sum_number, c)
    return final_result

a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
