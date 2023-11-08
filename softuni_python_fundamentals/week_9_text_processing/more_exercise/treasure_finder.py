key = [int(x) for x in input().split()]

user_command = input()
index = 0
new_string_list = []

while user_command != "find":
    new_string = ""
    for char in user_command:
        if index == len(key):
            index = 0
        new_ord = ord(char) - key[index]
        new_string += chr(new_ord)
        index += 1
    new_string_list.append(new_string)
    index = 0
    user_command = input()

for string in new_string_list:
    type = ""
    coordinates = ""
    start_index_type = 0
    end_index_type = 0
    start_index_coordinates = 0
    end_index_coordinates = 0
    for idx in range(len(string)):
        if string[idx] == "&":
            if start_index_type == 0:
                start_index_type = idx
            else:
                end_index_type = idx
        if string[idx] == "<":
            start_index_coordinates = idx
        if string[idx] == ">":
            end_index_coordinates = idx
    type = string[start_index_type + 1:end_index_type]
    coordinates = string[start_index_coordinates + 1:end_index_coordinates]
    print(f"Found {type} at {coordinates}")
