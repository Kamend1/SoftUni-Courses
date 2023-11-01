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

sorted_dwarves = sorted(dwarves.items(), key=lambda x: (max(v for v in x[1].values()), len(x[0])), reverse=True)

for hat_color, names in sorted_dwarves:
    for name, attributes in names.items():
        print(f"({hat_color}) {name} <-> {attributes}")
