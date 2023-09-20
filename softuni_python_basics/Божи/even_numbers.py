sum_even = 0

for i in range(10):
    num = int(input("Въведете число: "))

    if num % 2 == 0:
        sum_even += num

print("Сборът на четните числа е:", sum_even)
