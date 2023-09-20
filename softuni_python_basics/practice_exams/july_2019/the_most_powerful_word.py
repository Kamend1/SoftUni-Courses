from math import floor
user_command = input()
current_score = 0
max_score = 0
most_powerful_word = ""

while user_command != "End of words":
    for charcter in user_command:
        current_score += ord(charcter)
    if user_command[0] == "a" or user_command[0] == "e" or user_command[0] == "i" \
                or user_command[0] == "o" or user_command[0] == "u" or user_command[0] == "y" \
                or user_command[0] == "A" or user_command[0] == "E" or user_command[0] == "I" \
                or user_command[0] == "O" or user_command[0] == "U" or user_command[0] == "Y":
        current_score *= len(user_command)
    else:
        current_score = floor(current_score / len(user_command))
    if current_score >= max_score:
        max_score = current_score
        most_powerful_word = user_command

    current_score = 0
    user_command = input()

print(f"The most powerful word is {most_powerful_word} - {max_score}")
