number_of_men = int(input())
number_of_women = int(input())
number_of_tables = int(input())
no_more_tables = False


for men in range(1, number_of_men + 1):
    for women in range(1, number_of_women + 1):
        number_of_tables -= 1
        print(f"({men} <-> {women})", end=" ")
        if number_of_tables == 0:
            no_more_tables = True
            break
    if no_more_tables:
        break
