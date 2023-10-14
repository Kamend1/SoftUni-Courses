treasure_chest = input().split("|")
user_command = input().split()

while user_command[0] != "Yohoho!":
    if user_command[0] == "Loot":
        for item in user_command[1:]:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif user_command[0] == "Drop":
        if 0 <= int(user_command[1]) < len(treasure_chest):
            current_item = treasure_chest[int(user_command[1])]
            treasure_chest.remove(current_item)
            treasure_chest.append(current_item)
    elif user_command[0] == "Steal":
        end_idx = len(treasure_chest) - 1 - int(user_command[1])
        if end_idx < 0:
            print(", ".join(treasure_chest))
            treasure_chest = []
        else:
            print(", ".join(treasure_chest[-int(user_command[1]):]))
            treasure_chest = treasure_chest[:end_idx + 1]


    user_command = input().split()

sum_item_length = 0

if treasure_chest:
    for item in treasure_chest:
        sum_item_length += len(item)
        average_length = sum_item_length / len(treasure_chest)
    print(f'Average treasure gain: {average_length:.2f} pirate credits.')
else:
    print(f"Failed treasure hunt.")
