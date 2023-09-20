def add_digits(number):
    list_of_digits = []
    while number > 0:
        digit = number % 10
        list_of_digits.append(digit)
        number //= 10

    return list_of_digits


number = int(input())
list_of_digits = add_digits(number)
list_of_digits.sort(reverse=True)

for digit in list_of_digits:
    print(digit, end="")
