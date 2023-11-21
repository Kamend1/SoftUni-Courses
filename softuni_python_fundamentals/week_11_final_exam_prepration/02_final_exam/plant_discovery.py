def rate(plant, rating, collection):
    collection[plant]['ratings'].append(rating)
    return collection

def update_rarity(plant, rarity, collection):
    collection[plant]['rarity'] = rarity
    return collection

def reset(plant, collection):
    collection[plant]['ratings'].clear()
    return collection

number_plants = int(input())
plant_collection = {}

for _ in range(number_plants):
    current_plant = input().split("<->")
    if current_plant[0] in plant_collection:
        plant_collection[current_plant[0]]['rarity'] = int(current_plant[1])
    else:
        plant_collection[current_plant[0]] = {'rarity': int(current_plant[1]), 'ratings': []}

while True:
    user_command = input()
    if user_command == "Exhibition":
        break
    action, tokens = user_command.split(": ")
    if action == "Rate":
        rated_plant, new_rating = tokens.split(" - ")
        if rated_plant not in plant_collection:
            print("error")
        else:
            plant_collection = rate(rated_plant, int(new_rating), plant_collection)
    elif action == "Update":
        updated_plant, new_rarity = tokens.split(" - ")
        if updated_plant not in plant_collection:
            print("error")
        else:
            plant_collection = update_rarity(updated_plant, new_rarity, plant_collection)
    elif action == "Reset":
        reset_plant = tokens
        if reset_plant not in plant_collection:
            print("error")
        else:
            plant_collection = reset(reset_plant, plant_collection)

print("Plants for the exhibition:")
for plant_name, values in plant_collection.items():
    if len(values['ratings']) > 0:
        print(f"- {plant_name}; Rarity: {values['rarity']}; "
              f"Rating: {(sum(values['ratings'])/len(values['ratings'])):.2f}")
    else:
        print(f"- {plant_name}; Rarity: {values['rarity']}; Rating: 0.00")
