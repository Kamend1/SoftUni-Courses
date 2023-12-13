def change(string, character, replacement):
    string = string.replace(character, replacement)
    return string

def includes(string, substring):
    if substring in string:
        result = True
    else:
        result = False
    return result


def end_with(string, substring):
    if string.endswith(substring):
        result = True
    else:
        result = False
    return result


def all_uppercase(string):
    string = string.upper()
    return string


def find_index(string, character):
    if character in string:
        return string.index(character)


def cut(string, start_index, length):
    end_index = start_index + length
    string = string[start_index:end_index]
    return string

current_string = input()

user_command = input()

while user_command != "Done":
    actions = user_command.split()

    if actions[0] == "Change":
        old_char = actions[1]
        new_char = actions[2]
        current_string = change(current_string, old_char, new_char)
        print(current_string)
    elif actions[0] == "Includes":
        string_to_check = actions[1]
        if includes(current_string, string_to_check):
            print("True")
        else:
            print("False")
    elif actions[0] == "End":
        string_to_check = actions[1]
        if end_with(current_string, string_to_check):
            print("True")
        else:
            print("False")
    elif actions[0] == "Uppercase":
        current_string = all_uppercase(current_string)
        print(current_string)
    elif actions[0] == "FindIndex":
        given_character = actions[1]
        result = find_index(current_string, given_character)
        print(result)
    elif actions[0] == "Cut":
        start_idx = int(actions[1])
        current_length = int(actions[2])
        current_string = cut(current_string, start_idx, current_length)
        print(current_string)

    user_command = input()
