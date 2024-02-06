from collections import deque

elf_energy = deque(int(x) for x in input().split())
num_materials = [int(x) for x in input().split()]
total_elf_energy = 0
number_toys_made = 0
turns = 0

while elf_energy and num_materials:
    while True:
        current_elf = elf_energy.popleft()
        if current_elf < 5:
            current_elf = None
            if not elf_energy:
                break
        else:
            break

    if not current_elf:
        break

    current_material = num_materials.pop()
    turns += 1

    if turns % 3 == 0 and turns % 5 != 0:
        current_material = int(current_material * 2)

        if current_elf >= current_material:
            number_toys_made += 2
            current_elf = current_elf - current_material + 1
            elf_energy.append(current_elf)
            total_elf_energy += current_material

        else:
            num_materials.append(int(current_material / 2))
            elf_energy.append(current_elf * 2)

    elif turns % 3 != 0 and turns % 5 == 0:

        if current_elf >= current_material:
            current_elf = current_elf - current_material
            elf_energy.append(current_elf)
            total_elf_energy += current_material

        else:
            num_materials.append(current_material)
            elf_energy.append(current_elf * 2)

    elif turns % 15 == 0:
        current_material = int(current_material * 2)

        if current_elf >= current_material:
            current_elf = current_elf - current_material
            elf_energy.append(current_elf)
            total_elf_energy += current_material

        else:
            num_materials.append(int(current_material / 2))
            elf_energy.append(current_elf * 2)

    else:

        if current_elf >= current_material:
            number_toys_made += 1
            current_elf = current_elf - current_material + 1
            elf_energy.append(current_elf)
            total_elf_energy += current_material

        else:
            num_materials.append(current_material)
            elf_energy.append(current_elf * 2)

print(f"Toys: {number_toys_made}")
print(f"Energy: {total_elf_energy:.0f}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if num_materials:
    print(f"Boxes left: {', '.join(str(x) for x in num_materials)}")
