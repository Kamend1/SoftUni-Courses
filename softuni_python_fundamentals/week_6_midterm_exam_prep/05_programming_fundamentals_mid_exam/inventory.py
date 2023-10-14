inventory = input().split(", ")

user_command = input()

while user_command != "Craft!":
    user_command = user_command.split(" - ")
    if user_command[0] == "Collect":
        if user_command[1] not in inventory:
            inventory.append(user_command[1])
    elif user_command[0] == "Drop":
        if user_command[1] in inventory:
            inventory.remove(user_command[1])
    elif user_command[0] == "Combine Items":
        item_list = user_command[1].split(":")
        if item_list[0] in inventory:
            index = inventory.index(item_list[0]) + 1
            inventory.insert(index, item_list[1])
    elif user_command[0] == "Renew":
        if user_command[1] in inventory:
            inventory.remove(user_command[1])
            inventory.append(user_command[1])

    user_command = input()

print(", ".join(inventory))
