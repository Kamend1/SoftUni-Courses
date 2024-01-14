from collections import deque

presents_magic_needed_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

crafted_toys = {}
presents_crafted = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    product = current_material * current_magic
    if product in presents_magic_needed_dict.keys():
        crafted_toy = presents_magic_needed_dict.get(product)
        if crafted_toy not in crafted_toys:
            crafted_toys[crafted_toy] = 0
        crafted_toys[crafted_toy] += 1
    elif product > 0:
        current_material += 15
        materials.append(current_material)
    elif product < 0:
        current_material += current_magic
        materials.append(current_material)
    elif product == 0:
        if current_material != 0:
            materials.append(current_material)
        if current_magic != 0:
            magic.appendleft(current_magic)

if 'Doll' in crafted_toys and 'Wooden train' in crafted_toys:
    presents_crafted = True

if 'Bicycle' in crafted_toys and 'Teddy bear' in crafted_toys:
    presents_crafted = True


if presents_crafted:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    materials.reverse()
    print_str = ', '.join(map(str, materials))
    print(f"Materials left: {print_str}")
if magic:
    print_str = ', '.join(map(str, magic))
    print(f"Magic left: {print_str}")
for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")
