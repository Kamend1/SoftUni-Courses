def move(number, string: str):
    moved_string = string[:number]
    string = string.replace(moved_string, "")
    string += moved_string
    return string


def insert_string(index, value, string: str):
    first_part_string = string[:index]
    second_part_string = string[index:]
    new_string = first_part_string + value + second_part_string
    return new_string


def replace_string(substring: str, replacement: str, string: str):
    string = string.replace(substring, replacement)
    return string


encrypted_string = input()
user_command = input()

while user_command != "Decode":
    user_command = user_command.split("|")
    if user_command[0] == "Move":
        number_of_letters = int(user_command[1])
        encrypted_string = move(number_of_letters, encrypted_string)
    elif user_command[0] == "Insert":
        index_to_insert, value_to_insert = int(user_command[1]), user_command[2]
        encrypted_string = insert_string(index_to_insert, value_to_insert, encrypted_string)
    elif user_command[0] == "ChangeAll":
        string_to_replace, replacement_string = user_command[1], user_command[2]
        encrypted_string = replace_string(string_to_replace, replacement_string, encrypted_string)

    user_command = input()

print(f"The decrypted message is: {encrypted_string}")
