user_command = input()
current_sum = 0
max_sum = 0
best_movie = ""
name_movie = ""

for i in range(7):
    if user_command == "STOP":
        break
    name_movie = user_command
    for character in name_movie:
        current_sum += ord(character)
        if 65 <= ord(character) <= 90:
            current_sum -= len(name_movie)
        elif 97 <= ord(character) <= 122:
            current_sum -= 2 * len(name_movie)

    if current_sum > max_sum:
        max_sum = current_sum
        best_movie = name_movie
    current_sum = 0
    if i == 6:
        break
    user_command = input()

if i == 6 and user_command != "STOP":
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {max_sum} ASCII sum.")
