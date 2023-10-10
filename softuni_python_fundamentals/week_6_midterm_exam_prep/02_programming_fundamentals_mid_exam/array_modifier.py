array = [int(x) for x in input().split()]

user_command = input()

while user_command != "end":
    user_command_list = user_command.split()
    if user_command_list[0] == "swap":
        first_index = int(user_command_list[1])
        second_index = int(user_command_list[2])
        array[first_index], array[second_index] = array[second_index], array[first_index]
    elif user_command_list[0] == "multiply":
        first_index = int(user_command_list[1])
        second_index = int(user_command_list[2])
        array[first_index] = array[first_index] * array[second_index]
    elif user_command_list[0] == "decrease":
        for idx in range(len(array)):
            array[idx] -= 1
    user_command = input()

print(*array, sep=", ")
