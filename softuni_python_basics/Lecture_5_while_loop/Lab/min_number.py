from sys import maxsize
user_input = input()
min_number = maxsize

while user_input != "Stop":
    if min_number > int(user_input):
        min_number = int(user_input)
        user_input = input()
    else:
        user_input = input()

print(min_number)
