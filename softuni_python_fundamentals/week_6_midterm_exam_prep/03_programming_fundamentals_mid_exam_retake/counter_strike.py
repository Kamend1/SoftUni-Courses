energy = int(input())
user_command = input()

won_battles_count = 0
energy_lost = False


while user_command != "End of battle":
    distance = int(user_command)
    if distance <= energy:
        energy -= distance
        won_battles_count += 1
    else:
        energy_lost = True
        break
    if won_battles_count != 0 and won_battles_count % 3 == 0:
        energy += won_battles_count
    user_command = input()

if energy_lost:
    print(f"Not enough energy! Game ends with {won_battles_count} won battles and {energy} energy")
else:
    print(f"Won battles: {won_battles_count}. Energy left: {energy}")
