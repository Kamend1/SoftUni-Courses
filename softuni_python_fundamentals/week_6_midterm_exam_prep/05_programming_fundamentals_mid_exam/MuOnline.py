health = 100
bitcoins = 0
room_counter = 0
dungeon_rooms = [list(s.split()) for s in input().split("|")]
hero_is_killed = False

for room in dungeon_rooms:
    if room[0] == "potion":
        if 100 - health <= int(room[1]):
            amount_healed = 100 - health
            health = 100
        else:
            amount_healed = int(room[1])
            health += amount_healed
        room_counter += 1
        print(f"You healed for {amount_healed} hp.")
        print(f"Current health: {health} hp.")
    elif room[0] == "chest":
        bitcoins += int(room[1])
        room_counter += 1
        print(f"You found {room[1]} bitcoins.")
    else:
        health -= int(room[1])
        if health > 0:
            print(f"You slayed {room[0]}.")
            room_counter += 1
        else:
            print(f"You died! Killed by {room[0]}.")
            hero_is_killed = True
            room_counter += 1
            break

if hero_is_killed:
    print(f'Best room: {room_counter}')
else:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
