dwarves = {}
hat_color_by_count = {}

while True:
    user_command = input().split(" <:> ")
    if user_command[0] == "Once upon a time":
        break

    dwarf_name = user_command[0]
    dwarf_color = user_command[1]
    dwarf_physics = int(user_command[2])

    if dwarf_color not in dwarves:
        dwarves[dwarf_color] = {}

    if dwarf_name not in dwarves[dwarf_color]:
        dwarves[dwarf_color][dwarf_name] = dwarf_physics
    else:
        if dwarves[dwarf_color][dwarf_name] < dwarf_physics:
            dwarves[dwarf_color][dwarf_name] = dwarf_physics

for hat_color, dwarf_list in dwarves.items():
    if hat_color not in hat_color_by_count:
        hat_color_by_count[hat_color] = 0
    for dwarf in dwarf_list.keys():
        hat_color_by_count[hat_color] += 1

hat_color_by_count = dict(sorted(hat_color_by_count.items(), key=lambda x: -x[1]))

ranked_hat_color_by_count = {}
counter = len(hat_color_by_count)
for hat_color in hat_color_by_count:
    if hat_color not in ranked_hat_color_by_count:
        ranked_hat_color_by_count[hat_color] = 0
    ranked_hat_color_by_count[hat_color] = counter
    counter -= 1

ranked_dwarves = {value: dwarves[key] for key, value in ranked_hat_color_by_count.items()}

sorted_dwarves_list = []

for hat_color, names in ranked_dwarves.items():
    for name, attributes in names.items():
        sorted_dwarves_list.append((hat_color, name, attributes))

sorted_dwarves_list.sort(key=lambda x: (-x[2], -x[0]))

result = []

for num, name, value in sorted_dwarves_list:
    color = next((color for color, number in ranked_hat_color_by_count.items() if number == num), num)
    result.append((color, name, value))

for tuple in result:
    print(f"({tuple[0]}) {tuple[1]} <-> {tuple[2]}")
