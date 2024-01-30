from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

healing_items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit',
}

textiles_empty = False
medicaments_empty = False

healing_items_crafted = {}

while True:
    if medicaments_empty:
        break
    if textiles_empty:
        break

    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    result = current_textile + current_medicament

    if result in healing_items:
        current_item = healing_items[result]
        if current_item not in healing_items_crafted:
            healing_items_crafted[current_item] = 0
        healing_items_crafted[current_item] += 1
    else:

        if result > 100:

            remaining_resource = result - 100
            result = 100
            current_item = healing_items[result]
            if current_item not in healing_items_crafted:
                healing_items_crafted[current_item] = 0
            healing_items_crafted[current_item] += 1
            if medicaments:
                medicament_to_replace = medicaments.pop() + remaining_resource
                medicaments.append(medicament_to_replace)

        else:
            current_medicament += 10
            medicaments.append(current_medicament)

    if not medicaments:
        medicaments_empty = True

    if not textiles:
        textiles_empty = True


if medicaments_empty and textiles_empty:
    print("Textiles and medicaments are both empty.")
elif medicaments_empty:
    print("Medicaments are empty.")
elif textiles_empty:
    print("Textiles are empty.")

sorted_dict = dict(sorted(healing_items_crafted.items(), key=lambda x: (-x[1], x[0])))

for k, v in sorted_dict.items():
    print(f"{k} - {v}")


if medicaments_empty and not textiles_empty:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

if textiles_empty and not medicaments_empty:
    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")
