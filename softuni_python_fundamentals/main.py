first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number):
    str_num = str(num)
    sum_even = 0
    sum_odd = 0
    for index in range(len(str_num)):
        if index % 2 == 0:
            sum_even += int(str_num[index])
        else:
            sum_odd += int(str_num[index])
    if sum_even == sum_odd == sum_even:
        print(num, end=' ')

