happy_year = int(input())


while True:
    happy_year += 1
    str_happy_year = str(happy_year)
    is_happy = True

    # Sort the digits of the year.
    arr_happy_year = []
    for num in str_happy_year:
        arr_happy_year.append(num)
    arr_happy_year.sort()

    # Check for repeated digits.
    for idx in range(len(arr_happy_year) - 1):
        if arr_happy_year[idx] == arr_happy_year[idx + 1]:
            is_happy = False
            break

    if is_happy:
        break

print(happy_year)
