dwarves = {}

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
        dwarves[dwarf_color][dwarf_name] = {"physics": dwarf_physics}
    else:
        dwarves[dwarf_color].pop(dwarf_name, {})
        dwarves[dwarf_color][dwarf_name] = {"physics": dwarf_physics}


sorted_dwarves = dict(sorted(dwarves.items(), key=lambda x: (-max(v['physics'] for v in x[1].values()), -len(x[1]))))

for hat_color, names in sorted_dwarves.items():
    for name, attributes in names.items():
        print(f"({hat_color}) {name} <-> {attributes['physics']}")
