def contains(string: str, substring: str):
    if substring in string:
        result = f"{string} contains {substring}"
    else:
        result = "Substring not found!"
    return result


def flip(string: str, case: str, start_index: int, end_index: int):
    if case == "Upper":
       result = string[:start_index]+string[start_index:end_index].upper()+string[end_index:]
    elif case == "Lower":
        result = string[:start_index]+string[start_index:end_index].lower()+string[end_index:]
    return result


def slice(string: str, start_index: int, end_index: int):
    result = string[:start_index] + string[end_index:]
    return result


raw_key = input()
user_command = input()

while user_command != "Generate":
    actions = user_command.split(">>>")
    if actions[0] == "Contains":
        current_result = contains(raw_key, actions[1])
        print(current_result)
    elif actions[0] == "Flip":
        current_result = flip(raw_key, actions[1], int(actions[2]), int(actions[3]))
        raw_key = current_result
        print(current_result)
    elif actions[0] == "Slice":
        current_result = slice(raw_key, int(actions[1]), int(actions[2]))
        raw_key = current_result
        print(current_result)
    user_command = input()

print(f"Your activation key is: {raw_key}")
