user_input_number = int(input())
# top line all cases
if user_input_number % 2 == 0:
    print("-" * ((user_input_number - 2) // 2) + "*" * 2 + "-" * ((user_input_number - 2) // 2))
elif user_input_number % 2 != 0:
    print("-" * ((user_input_number - 1) // 2) + "*" + "-" * ((user_input_number - 1) // 2))

# body above middle line
if user_input_number % 2 == 0 and user_input_number > 2:
    for i in range(int((user_input_number / 2) - 2)):
        reverse_row = int((user_input_number / 2) - 1) - (i + 1)
        left_str = "-" * reverse_row + "*"
        middle_str = "--" * (i + 1)
        right_str = "*" + "-" * reverse_row
        print(left_str + middle_str + right_str)
elif user_input_number % 2 != 0 and user_input_number > 2:
    for i in range(int((user_input_number / 2) - 1)):
        reverse_row = int((user_input_number / 2)) - (i + 1)
        left_str = "-" * reverse_row + "*"
        middle_str = "-" * (i + 1) + "-" * i
        right_str = "*" + "-" * reverse_row
        print(left_str + middle_str + right_str)

# middle line for cases starting 3
if user_input_number > 2:
    str_middle_number = "*" + "-" * (user_input_number - 2) + "*"
    print(str_middle_number)

# body below middle line
if user_input_number % 2 == 0 and user_input_number > 2:
    for j in range(int((user_input_number / 2) - 2), 0, -1):
        reverse_row = int((user_input_number / 2) - 2) - (j - 1)
        left_str = "-" * reverse_row + "*"
        middle_str = "--" * j
        right_str = "*" + "-" * reverse_row
        print(left_str + middle_str + right_str)
elif user_input_number % 2 != 0 and user_input_number > 2:
    for y in range(int((user_input_number / 2)) - 1, 0, -1):
        reverse_row = int((user_input_number / 2)) - (y)
        left_str = "-" * reverse_row + "*"
        middle_str = "-" * (y - 1) + "-" * y
        right_str = "*" + "-" * reverse_row
        print(left_str + middle_str + right_str)

# bottom line for cases starting 3
if user_input_number % 2 == 0 and user_input_number > 2:
    print("-" * ((user_input_number - 2) // 2) + "*" * 2 + "-" * ((user_input_number - 2) // 2))
elif user_input_number % 2 != 0 and user_input_number > 2:
    print("-" * ((user_input_number - 1) // 2) + "*" + "-" * ((user_input_number - 1) // 2))
