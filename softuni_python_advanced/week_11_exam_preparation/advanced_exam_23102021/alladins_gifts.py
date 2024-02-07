from collections import deque

materials = [int(x) for x in input().split()]
genie_magic_level = deque(int(x) for x in input().split())
products_crafted = {}


while True:
    if not materials or not genie_magic_level:
        break

    current_material = materials.pop()
    current_magic = genie_magic_level.popleft()
    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            result = 2 * current_material + 3 * current_magic
        else:
            result *= 2
    elif result > 499:
        result /= 2

    if 100 <= result <= 199:
        products_crafted['Gemstone'] = products_crafted.get('Gemstone', 0) + 1
    elif 200 <= result <= 299:
        products_crafted['Porcelain Sculpture'] = products_crafted.get('Porcelain Sculpture', 0) + 1
    elif 300 <= result <= 399:
        products_crafted['Gold'] = products_crafted.get('Gold', 0) + 1
    elif 400 <= result <= 499:
        products_crafted['Diamond Jewellery'] = products_crafted.get('Diamond Jewellery', 0) + 1

if ('Gemstone' in products_crafted and 'Porcelain Sculpture' in products_crafted) \
        or ('Gold' in products_crafted and 'Diamond Jewellery' in products_crafted):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if genie_magic_level:
    print(f"Magic left: {', '.join(str(x) for x in genie_magic_level)}")

products_crafted = dict(sorted(products_crafted.items(), key=lambda x: x[0]))
for k, v in products_crafted.items():
    print(f"{k}: {v}")
