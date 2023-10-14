houses = [int(x) for x in input().split("@")]
user_command = input().split()
current_index = 0

while user_command[0] != "Love!":
    if user_command[0] == "Jump":
        if current_index + int(user_command[1]) >= len(houses):
            current_index = 0
        else:
            current_index = current_index + int(user_command[1])
        if houses[current_index] == 0:
            print(f"Place {current_index} already had Valentine's day.")
        else:
            houses[current_index] -= 2
            if houses[current_index] == 0:
                print(f"Place {current_index} has Valentine's day.")

    user_command = input().split()

failed_counter = 0
print(f"Cupid's last position was {current_index}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    for idx in range(len(houses)):
        if houses[idx] != 0:
            failed_counter += 1
    print(f"Cupid has failed {failed_counter} places.")
