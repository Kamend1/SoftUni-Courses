num_dragons = int(input())

default_damage = 45
default_health = 250
default_armor = 10
dragons_dict = {}


for i in range(num_dragons):
    user_input = input().split()
    if user_input[0] not in dragons_dict:
        dragons_dict[user_input[0]] = {}
    if user_input[1] not in dragons_dict[user_input[0]]:
        dragons_dict[user_input[0]][user_input[1]] = {}

    dragons_dict[user_input[0]][user_input[1]] = {"damage": user_input[2], "health": user_input[3],
                                                  "armor": user_input[4]}

for dragon_color, names in dragons_dict.items():
    for dragon_name, attributes in names.items():
        if attributes["damage"] == "null":
            attributes["damage"] = default_damage
        if attributes["health"] == "null":
            attributes["health"] = default_health
        if attributes["armor"] == "null":
            attributes["armor"] = default_armor

for dragon_color, names in dragons_dict.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    counter = 0
    for dragon_name, attributes in names.items():
        total_damage += int(attributes['damage'])
        total_health += int(attributes['health'])
        total_armor += int(attributes['armor'])
        counter += 1
    average_damage = total_damage / counter
    average_health = total_health / counter
    average_armor = total_armor / counter
    print(f"{dragon_color}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    for dragon_name,attributes in sorted(names.items()):
        damage = dragons_dict[dragon_color][dragon_name]["damage"]
        health = dragons_dict[dragon_color][dragon_name]["health"]
        armor = dragons_dict[dragon_color][dragon_name]["armor"]
        print(f"-{dragon_name} -> damage: {damage}, health: {health}, armor: {armor}")
