initial_energy = 100
initial_coins = 100
events_list = list(input().split("|"))
event_type = []
event_value = []
energy_gained = 0
finished_day = True

for event in events_list:
    event_type.append(event.split("-")[0])
    event_value.append(int(event.split("-")[1]))
for idx in range(len(event_type)):
    if event_type[idx] == "rest":
        if initial_energy + event_value[idx] >= 100:
            energy_gained = 100 - initial_energy
            initial_energy = 100
        else:
            energy_gained = event_value[idx]
            initial_energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event_type[idx] == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value[idx]
            print(f"You earned {event_value[idx]} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= event_value[idx]:
            initial_coins -= event_value[idx]
            print(f"You bought {event_type[idx]}.")
        else:
            finished_day = False
            print(f"Closed! Cannot afford {event_type[idx]}.")
            break

if finished_day:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
