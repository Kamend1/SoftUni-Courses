def insert_space(index, string):
    result = ""
    if index < len(string) - 1:
        result = string[:index] + " " + string[index:]
    elif index == len(string) -1:
        result = string[:index] + " "
    return result


def reverse_substring(substring, string):
    result = ""
    reversed_string = substring[::-1]
    if substring in string:
        result += string.replace(substring, "", 1)
        result += reversed_string
    else:
        result += "error"
    return result


def change_all(substring, replacement, string):
    result = ""
    while substring in string:
        string = string.replace(substring, replacement)
    result += string
    return result


secret_message = input()
user_command = input()

while user_command != "Reveal":
    actions = user_command.split(":|:")
    if actions[0] == "InsertSpace":
        current_result = insert_space(int(actions[1]), secret_message)
        secret_message = current_result
        print(secret_message)
    elif actions[0] == "Reverse":
        current_result = reverse_substring(actions[1], secret_message)
        if current_result == "error":
            print(current_result)
        else:
            secret_message = current_result
            print(secret_message)
    elif actions[0] == "ChangeAll":
        current_result = change_all(actions[1], actions[2], secret_message)
        secret_message = current_result
        print(secret_message)

    user_command = input()

print(f"You have a new text message: {secret_message}")
