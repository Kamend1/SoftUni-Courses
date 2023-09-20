def calc_factoriel(number):
    if number == 0:
        return 1
    return number * calc_factoriel(number - 1)

number = int(input())

print(calc_factoriel(number))
