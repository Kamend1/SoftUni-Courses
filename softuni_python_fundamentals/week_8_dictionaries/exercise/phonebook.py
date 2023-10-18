phonebook = {}

while True:
    user_command = input()
    if user_command.isdigit():
        search_attempts = int(user_command)
        break
    else:
        user_command_list = user_command.split("-")
        if user_command_list[0] not in phonebook.keys():
            phonebook[user_command_list[0]] = 0
        phonebook[user_command_list[0]] = user_command_list[1]

for i in range(search_attempts):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
