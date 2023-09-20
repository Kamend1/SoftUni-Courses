variable_a1 = int(input())
variable_a2 = int(input())
variable_n = int(input())

for first_character in range(variable_a1,variable_a2):
    for second_character in range(1, variable_n):
        for third_character in range(1, int(variable_n / 2)):
            if first_character % 2 != 0 and (first_character + second_character + third_character) % 2 != 0:
                print(f"{chr(first_character)}-{second_character}{third_character}{first_character}")
