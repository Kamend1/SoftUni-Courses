def count_destroyed_ships(battle_field, ship_attacks, counter_destroyed):
    for attack in ship_attacks:
        row = int(attack[0])
        column = int(attack[2])
        if battle_field[row][column] != "0":
            new_ship_health = str(int(battle_field[row][column]) - 1)
            if new_ship_health == "0":
                counter_destroyed += 1
            battle_field[row][column] = new_ship_health
    return counter_destroyed


field_rows = int(input())
battle_field = []

for row in range(field_rows):
    battle_field.append(list(input().split()))

ship_attacks = list(input().split())
counter_destroyed = 0

counter_destroyed = count_destroyed_ships(battle_field, ship_attacks, counter_destroyed)
print(counter_destroyed)
