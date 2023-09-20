from sys import maxsize
user_input = input()
max_number = -maxsize

while user_input != "Stop":
    if max_number < int(user_input):
        max_number = int(user_input)
    user_input = input()

print(max_number)
