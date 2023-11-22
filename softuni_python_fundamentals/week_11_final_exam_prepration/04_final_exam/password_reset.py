def take_odd(string: str):
    result = ""
    for index in range(len(string)):
        if index % 2 != 0:
            result += string[index]
    return result

def cut(string: str, index: int, length: int):
    result = ""
    substring = string[index:index + length]
    result += string.replace(substring, "", 1)
    return result

def substitute(string: str, substring: str, substitute: str):
    result = ""
    if substring in string:
        result += string.replace(substring, substitute)
    else:
        result += "Nothing to replace!"
    return result

password = input()
user_command = input()

while user_command != "Done":
    actions = user_command.split(" ")
    if actions[0] == "TakeOdd":
        current_result = take_odd(password)
        password = current_result
        print(password)
    elif actions[0] == "Cut":
        current_result = cut(password, int(actions[1]), int(actions[2]))
        password = current_result
        print(password)
    elif actions[0] == "Substitute":
        current_result = substitute(password, actions[1], actions[2])
        if current_result == "Nothing to replace!":
            print(current_result)
        else:
            password = current_result
            print(password)
    user_command = input()

print(f"Your password is: {password}")
