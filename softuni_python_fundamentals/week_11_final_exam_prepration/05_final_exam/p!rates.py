def plunder(collection: dict, town: str, num_people: int, amount: int):
    result = ""
    collection[town]['people'] -= num_people
    collection[town]['gold'] -= amount
    result += f"{town} plundered! {amount} gold stolen, {num_people} citizens killed."
    if collection[town]['people'] == 0 or collection[town]['gold'] == 0:
        collection.pop(town)
        result += f"\n{town} has been wiped off the map!"
    return result

def prosper(collection: dict, town: str, amount: int):
    result = ""
    if amount >= 0:
        collection[town]['gold'] += amount
        result += f"{amount} gold added to the city treasury. {town} now has {collection[town]['gold']} gold."
    else:
        result += "Gold added cannot be a negative number!"
    return result


cities = {}

while True:
    user_command = input()
    if user_command == 'Sail':
        break
    city, people, gold = user_command.split("||")
    if city not in cities:
        cities[city] = {'people': int(people), 'gold': int(gold)}
    else:
        cities[city]['people'] += int(people)
        cities[city]['gold'] += int(gold)

while True:
    action_input = input().split("=>")
    if action_input[0] == 'End':
        break
    elif action_input[0] == "Plunder":
        current_result = plunder(cities, action_input[1], int(action_input[2]), int(action_input[3]))
        print(current_result)
    elif action_input[0] == "Prosper":
        current_result = prosper(cities, action_input[1], int(action_input[2]))
        print(current_result)

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, values in cities.items():
        print(f"{city} -> Population: {values['people']} citizens, Gold: {values['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
