def merge_elements(start_idx: int, end_idx: int, element_list: list):
    concatenated_string = ""
    removed_strings = []
    if start_idx < 0:
        start_idx = 0
    if start_idx > len(element_list) - 1:
        start_idx = len(element_list) - 2
    if end_idx >= len(element_list) - 1:
        end_idx = len(element_list) - 1
    if end_idx < 0:
        end_idx = 1
    for i in range(start_idx, end_idx + 1):
        removed_strings.append(element_list[i])
    concatenated_string = "".join(removed_strings)
    for item in removed_strings:
        element_list.remove(item)
    element_list.insert(start_index, concatenated_string)
    return element_list


def divide_element(idx: int, number_parts: int, element_list: list):
    string_to_be_divided = element_list[idx]
    part_length = len(string_to_be_divided) // number_parts
    parts_of_string = []
    idx_start = 0
    idx_end = 0
    for i in range(number_parts - 1):
        idx_start = i * part_length
        idx_end = (i + 1) * part_length
        part = string_to_be_divided[idx_start:idx_end]
        parts_of_string.append(part)
    if idx_end <= len(string_to_be_divided):
        last_part = string_to_be_divided[idx_end:]
        parts_of_string.append(last_part)

    element_list.pop(idx)
    for j in range(len(parts_of_string)):
        element_list.insert(idx + j, parts_of_string[j])
    return element_list

data_elements = input().split()

user_command = input()

while user_command != "3:1":
    user_command_list = user_command.split()
    if user_command_list[0] == "merge":
        start_index = int(user_command_list[1])
        end_index = int(user_command_list[2])
        merge_elements(start_index, end_index, data_elements)
    elif user_command_list[0] == "divide":
        index = int(user_command_list[1])
        parts = int(user_command_list[2])
        divide_element(index, parts, data_elements)
    user_command = input()

print(*data_elements, sep=" ")
