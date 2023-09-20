number_n = int(input())
valid_combination_found = False

if number_n % 5 == 0 and number_n % 3 == 0:
    for a in range(1, 10):
        if valid_combination_found == True:
            break
        for b in range(9, a - 1, -1):
            if valid_combination_found == True:
                break
            for c in range(10):
                if valid_combination_found == True:
                    break
                for d in range(9, c - 1, -1):
                    if valid_combination_found == True:
                        break
                    if (a + b + c + d) == (a * b * c * d) or (a * b * c * d) // (a + b + c + d) == 3:
                        if a > d or b > c:
                            print(f"{d}{c}{b}{a}")
                            valid_combination_found = True
                            break
                        else:
                            print(f"{a}{b}{c}{d}")
                            valid_combination_found = True
                            break
elif number_n % 5 == 0 and not number_n % 3 == 0:
    for a in range(1, 10):
        if valid_combination_found == True:
            break
        for b in range(9, a - 1, -1):
            if valid_combination_found == True:
                break
            for c in range(10):
                if valid_combination_found == True:
                    break
                for d in range(9, c - 1, -1):
                    if valid_combination_found == True:
                        break
                    if (a + b + c + d) == (a * b * c * d):
                        print(f"{a}{b}{c}{d}")
                        valid_combination_found = True
                        break
elif not number_n % 5 == 0 and number_n % 3 == 0:
    for a in range(1, 10):
        if valid_combination_found == True:
            break
        for b in range(9, a - 1, -1):
            if valid_combination_found == True:
                break
            for c in range(10):
                if valid_combination_found == True:
                    break
                for d in range(9, c - 1, -1):
                    if valid_combination_found == True:
                        break
                    if (a * b * c * d) // (a + b + c + d) == 3:
                        print(f"{d}{c}{b}{a}")
                        valid_combination_found = True
                        break
elif not number_n % 5 == 0 and not number_n % 3 == 0:
    print("Nothing found")
