number_n = int(input())
str_n = str(number_n)
valid_combination_found = False

if number_n < 100:
    print("Nothing found")
elif number_n > 1000:
    print("Nothing found")
else:
    for a in range(1, 10):
        if valid_combination_found:
            break
        for b in range(9, a - 1, -1):
            if valid_combination_found:
                break
            for c in range(10):
                if valid_combination_found:
                    break
                for d in range(9, c - 1, -1):
                    if valid_combination_found:
                        break
                    if (a * b * c * d) // (a + b + c + d) == 3 and number_n % 3 == 0:
                        print(f"{d}{c}{b}{a}")
                        valid_combination_found = True
                    if (a + b + c + d) == (a * b * c * d) and number_n % 5 == 0:
                        print(f"{a}{b}{c}{d}")
                        valid_combination_found = True


if not valid_combination_found and 100 < number_n < 1000:
    print("Nothing found")
