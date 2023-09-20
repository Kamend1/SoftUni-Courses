interval_beginning = int(input())
interval_end = int(input())

beginning_str = str(interval_beginning)
end_str = str(interval_end)

for first_character in range(int(beginning_str[0]), int(end_str[0]) + 1):
    if first_character % 2 == 0:
        continue
    for second_character in range(int(beginning_str[1]), int(end_str[1]) + 1):
        if second_character % 2 == 0:
            continue
        for third_character in range(int(beginning_str[2]), int(end_str[2]) + 1):
            if third_character % 2 == 0:
                continue
            for fourth_character in range(int(beginning_str[3]), int(end_str[3]) + 1):
                if fourth_character % 2 == 0:
                    continue
                print(f"{first_character}{second_character}{third_character}{fourth_character}", end=" ")
