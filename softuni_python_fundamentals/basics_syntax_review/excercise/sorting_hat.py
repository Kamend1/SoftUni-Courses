while True:
    user_input = input()
    if user_input == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if user_input == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(user_input) < 5:
        print(f"{user_input} goes to Gryffindor.")
    elif len(user_input) == 5:
        print(f"{user_input} goes to Slytherin.")
    elif len(user_input) == 6:
        print(f"{user_input} goes to Ravenclaw.")
    else:
        print(f"{user_input} goes to Hufflepuff.")
