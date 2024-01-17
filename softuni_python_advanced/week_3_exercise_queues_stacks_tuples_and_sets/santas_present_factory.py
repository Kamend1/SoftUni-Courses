from collections import deque

presents_magic_needed_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

crafted_toys = []
presents_crafted = False

while materials and magic:
    current_material = materials.pop() if magic[0] or not materials[-1] else 0
    current_magic = magic.popleft() if current_material or not magic[0] else 0

    if not current_magic:
        continue

    product = current_material * current_magic
    if product in presents_magic_needed_dict.keys():
        crafted_toys.append(presents_magic_needed_dict.get(product))
    elif product > 0:
        current_material += 15
        materials.append(current_material)
    elif product < 0:
        current_material += current_magic
        materials.append(current_material)

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
[print(f"{toy}: {crafted_toys.count(toy)}") for toy in sorted(set(crafted_toys))]
