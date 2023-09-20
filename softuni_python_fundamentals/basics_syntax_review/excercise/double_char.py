user_input = input()
characters = []

while user_input != "End":
    if user_input == "SoftUni":
        user_input = input()
    for character in user_input:
        characters.append(character)
        characters.append(character)


    new_string = "".join(characters)
    print(new_string)
    characters = []
    user_input = input()
