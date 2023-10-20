def register(name, plate, user_dict):
    if name in user_dict.keys():
        result = f"ERROR: already registered with plate number {user_dict[name]}"
    else:
        user_dict[name] = plate
        result = f"{name} registered {plate} successfully"
    return result


def unregister(name, user_dict):
    if name not in user_dict.keys():
        result = f"ERROR: user {name} not found"
    else:
        del user_dict[name]
        result = f"{name} unregistered successfully"
    return result


number_commands = int(input())
registry_dict = {}

for i in range(number_commands):
    user_command = input().split()
    if user_command[0] == "register":
        result = register(user_command[1], user_command[2], registry_dict)
        print(result)
    elif user_command[0] == "unregister":
        result = unregister(user_command[1], registry_dict)
        print(result)

for username, license_plate_number in registry_dict.items():
    print(f"{username} => {license_plate_number}")
