letter_begin_interval = input()
letter_end_interval = input()
letter_exclude_combo = input()
counter_valid_combo = 0
letter_combo = ""


for first_letter in range(ord(letter_begin_interval), ord(letter_end_interval) + 1):
    for middle_letter in range(ord(letter_begin_interval), ord(letter_end_interval) + 1):
        for last_letter in range(ord(letter_begin_interval), ord(letter_end_interval) + 1):
            if chr(first_letter) != letter_exclude_combo and chr(middle_letter) != letter_exclude_combo \
                    and chr(last_letter) != letter_exclude_combo:

                letter_combo = chr(first_letter) + chr(middle_letter) + chr(last_letter)
                counter_valid_combo += 1
                print(letter_combo, end=" ")

print(counter_valid_combo)
