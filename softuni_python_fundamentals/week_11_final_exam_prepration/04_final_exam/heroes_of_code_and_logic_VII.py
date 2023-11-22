def cast_spell(collection: dict, hero: str, m_points: int, spell: str):
    result = ""
    if collection[hero]['mana points'] >= m_points:
        collection[hero]['mana points'] -= m_points
        result += f"{hero} has successfully cast {spell} and now has {collection[hero]['mana points']} MP!"
    else:
        result += f"{hero} does not have enough MP to cast {spell}!"
    return result


def take_damage(collection: dict, hero: str, damage: int, attacker: str):
    result = ""
    collection[hero]['hit points'] -= damage
    if collection[hero]['hit points'] > 0:
        result += f"{hero} was hit for {damage} HP by {attacker} and now has {collection[hero]['hit points']} HP left!"
    else:
        result += f"{hero} has been killed by {attacker}!"
        collection.pop(hero)
    return result


def recharge(collection: dict, hero: str, amount: int):
    result = ""
    if collection[hero]['mana points'] + amount > 200:
        amount = 200 - collection[hero]['mana points']
        collection[hero]['mana points'] = 200
    else:
        collection[hero]['mana points'] += amount
    result += f"{hero} recharged for {amount} MP!"
    return result


def heal(collection: dict, hero: str, amount: int):
    result = ""
    if collection[hero]['hit points'] + amount > 100:
        amount = 100 - collection[hero]['hit points']
        collection[hero]['hit points'] = 100
    else:
        collection[hero]['hit points'] += amount
    result += f"{hero} healed for {amount} HP!"
    return result


number_heroes = int(input())
heroes_collection = {}

for _ in range(number_heroes):
    hero_name, hit_points, mana_points = input().split(" ")
    heroes_collection[hero_name] = {'hit points': int(hit_points), 'mana points': int(mana_points)}

user_command = input()

while user_command != "End":
    actions = user_command.split(" - ")
    if actions[0] == "CastSpell":
        current_result = cast_spell(heroes_collection, actions[1], int(actions[2]), actions[3])
        print(current_result)
    elif actions[0] == "TakeDamage":
        current_result = take_damage(heroes_collection, actions[1], int(actions[2]), actions[3])
        print(current_result)
    elif actions[0] == "Recharge":
        current_result = recharge(heroes_collection, actions[1], int(actions[2]))
        print(current_result)
    elif actions[0] == "Heal":
        current_result = heal(heroes_collection, actions[1], int(actions[2]))
        print(current_result)

    user_command = input()

for hero, values in heroes_collection.items():
    print(f"{hero}\n HP: {values['hit points']}\n MP: {values['mana points']}")
