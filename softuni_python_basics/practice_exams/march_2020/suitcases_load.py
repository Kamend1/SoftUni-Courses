volume_capacity = float(input())
user_command = input()
number_suitcases = 0
suitcase_counter = 0
no_more_space = False


while user_command != "End":
    current_volume = float(user_command)
    suitcase_counter += 1
    if suitcase_counter % 3 == 0:
        current_volume *= 1.10
    if volume_capacity < current_volume:
        no_more_space = True
        break
    number_suitcases += 1
    volume_capacity -= current_volume
    user_command = input()

if no_more_space:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {number_suitcases} suitcases loaded.")
