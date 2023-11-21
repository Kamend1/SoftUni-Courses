import re


def define_demon_health(name):
    letters_in_demon_name = re.findall(r"[^0-9\/\*\+\-\.]", name)
    result = 0
    for letter in letters_in_demon_name:
        result += ord(letter)
    return result


def define_demon_damage(name):
    result = 0
    mult_div_search = re.findall(r"[\/, *]", name)
    number_search = re.findall(r"[+\-]?\d+(?:\.\d+)?", name)

    for number in number_search:
        result += float(number)

    for operator in mult_div_search:
        if operator == '/':
            result /= 2
        elif operator == '*':
            result *= 2

    return result


demons_list = input().split(",")
demons_character_list = []

for demon in demons_list:
    demon_name = demon.strip()
    demons_health = define_demon_health(demon_name)
    demons_damage = define_demon_damage(demon_name)
    demons_character_list.append((demon_name, demons_health, demons_damage))

demons_character_list = sorted(demons_character_list)
for demon in demons_character_list:
    print(f"{demon[0]} - {demon[1]} health, {demon[2]:.2f} damage")
