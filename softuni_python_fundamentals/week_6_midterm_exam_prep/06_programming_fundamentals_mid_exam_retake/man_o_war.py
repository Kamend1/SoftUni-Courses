pirate_ship = [int(s) for s in input().split(">")]
warship = [int(s) for s in input().split(">")]
max_section_health = int(input())
user_command = input().split()
game_not_ended = True

while user_command[0] != "Retire":
    count_need_repair = 0
    if user_command[0] == "Fire":
        if 0 <= int(user_command[1]) < len(warship):
            warship[int(user_command[1])] -= int(user_command[2])
            if warship[int(user_command[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                game_not_ended = False
                break
    if user_command[0] == "Status":
        for section in pirate_ship:
            if section < max_section_health * 0.20:
                count_need_repair += 1
        print(f"{count_need_repair} sections need repair.")
    if user_command[0] == "Repair":
        if 0 <= int(user_command[1]) < len(pirate_ship):
            if int(user_command[2]) > max_section_health - pirate_ship[int(user_command[1])]:
                pirate_ship[int(user_command[1])] = max_section_health
            else:
                pirate_ship[int(user_command[1])] += int(user_command[2])
    if user_command[0] == "Defend":
        start_idx = int(user_command[1])
        end_idx = int(user_command[2])
        if 0 <= start_idx < len(pirate_ship) and 0 <= end_idx < len(pirate_ship):
            while start_idx <= end_idx:
                pirate_ship[start_idx] -= int(user_command[3])
                if pirate_ship[start_idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_not_ended = False
                    break
                start_idx += 1

    user_command = input().split()

if game_not_ended:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
