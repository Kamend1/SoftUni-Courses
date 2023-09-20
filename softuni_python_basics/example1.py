for number_n in range(100, 1001):
    str_n = str(number_n)
    valid_combination_found = False

    if number_n < 100:
        continue
    elif number_n > 1000:
        continue
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
                        if (a * b * c * d) // (a + b + c + d) == 3 and number_n % 3 == 0:
                            print(f"For number_n = {number_n}: {d}{c}{b}{a}")
                            valid_combination_found = True
                            break
                        if (a + b + c + d) == (a * b * c * d) and number_n % 5 == 0:
                            print(f"For number_n = {number_n}: {a}{b}{c}{d}")
                            valid_combination_found = True
                            break

    if not valid_combination_found:
        print(f"For number_n = {number_n}: Nothing found")
int(str_n[len(str_n)]) == 5: