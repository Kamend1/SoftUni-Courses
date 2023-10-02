def calc_factoriel(number):
    if number == 0:
        return 1
    return number * calc_factoriel(number - 1)

num_1 = int(input())
num_2 = int(input())

result = calc_factoriel(num_1) / calc_factoriel(num_2)

print(f"{result:.2f}")
