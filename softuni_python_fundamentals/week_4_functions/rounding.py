def rounded_number(num):
    result = round(num)
    return result

numbers_list = [float(x) for x in input().split()]
rounded_numbers = []

for number in numbers_list:
    rounded_numbers.append(rounded_number(number))

print(rounded_numbers)
