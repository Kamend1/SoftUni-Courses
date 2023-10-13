def shoot_target(index, power, target_list):
    if 0 <= index < len(target_list):
        target_list[index] -= power
        if target_list[index] <= 0:
            target_list.pop(index)


def add_target(index, value, target_list):
    if 0 <= index < len(target_list):
        target_list.insert(index, value)
    else:
        print("Invalid placement!")


def strike_targets(index, radius, target_list):
    start_index = index - radius
    end_index = index + radius
    if end_index <= len(target_list) and start_index >= 0:
        target_list[start_index:end_index + 1] = []
    else:
        print("Strike missed!")


targets = [int(x) for x in input().split()]
user_command = input()

while user_command != "End":
    user_command_list = user_command.split()
    if user_command_list[0] == "Shoot":
        shoot_target(int(user_command_list[1]), int(user_command_list[2]), targets)
    elif user_command_list[0] == "Add":
        add_target(int(user_command_list[1]), int(user_command_list[2]), targets)
    elif user_command_list[0] == "Strike":
        strike_targets(int(user_command_list[1]), int(user_command_list[2]), targets)
    user_command = input()

print(*targets, sep="|")
