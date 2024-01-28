first_line = input()
try:
    second_line = int(input())
    print(first_line * second_line)
except ValueError:
    print("Variable times must be an integer")
