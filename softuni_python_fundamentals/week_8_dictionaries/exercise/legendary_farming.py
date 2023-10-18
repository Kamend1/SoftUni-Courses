valuable_materials = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

junk_materials = {}
item_not_found = True


while item_not_found:
    user_command = input().split()
    for idx in range(len(user_command)):
        if idx % 2 != 0:
            string_item = str(user_command[idx]).lower()
            quantity = int(user_command[idx - 1])
            if string_item in valuable_materials.keys():
                valuable_materials[string_item] += quantity
                if valuable_materials["shards"] >= 250:
                    print("Shadowmourne obtained!")
                    valuable_materials["shards"] -= 250
                    item_not_found = False
                    break
                if valuable_materials["fragments"] >= 250:
                    print("Valanyr obtained!")
                    valuable_materials["fragments"] -= 250
                    item_not_found = False
                    break
                if valuable_materials["motes"] >= 250:
                    print("Dragonwrath obtained!")
                    valuable_materials["motes"] -= 250
                    item_not_found = False
                    break
            else:
                if string_item not in junk_materials.keys():
                    junk_materials[string_item] = 0
                junk_materials[string_item] += quantity


for item, qty in valuable_materials.items():
    print(f"{str(item).lower()}: {qty}")
for item, qty in junk_materials.items():
    print(f"{str(item).lower()}: {qty}")
