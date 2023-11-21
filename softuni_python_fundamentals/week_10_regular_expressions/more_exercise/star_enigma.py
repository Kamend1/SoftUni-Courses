import re

pattern_number_letters = r"(?i)[s, t, a, r]"
pattern_decrypted = r"""[^\@, \-, \!, \:, \>]*(\@(?P<planet>[a-zA-Z]+))[^\@, \-, \!, \:, \>]*(\:(?P<population>[
0-9]+))[^\@, \-, \!, \:, \>]*(\!(?P<attack_type>[A, D])\!)[^\@, \-, \!, \:, \>]*(\->(?P<soldier_count>\d+))"""

attacked_planets = []
destroyed_planets = []
number_of_messages = int(input())

for message in range(number_of_messages):
    encrypted_message = input()
    matches = re.findall(pattern_number_letters, encrypted_message)
    count = len(matches)
    decrypted_message = ""

    for char in encrypted_message:
        new_char = chr(ord(char) - count)
        decrypted_message += new_char
    match_attack = re.search(pattern_decrypted, decrypted_message)
    if match_attack:
        planet = match_attack.group('planet')
        population = match_attack.group('population')
        attack_type = match_attack.group('attack_type')
        soldier_count = match_attack.group('soldier_count')
        if attack_type == 'A':
            attacked_planets.append(planet)
        elif attack_type == 'D':
            destroyed_planets.append(planet)

print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")
