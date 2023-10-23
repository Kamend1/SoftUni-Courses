def add_player(name: str, skill: str, value: int, pool: dict):
    if name not in pool.keys():
        pool[name] = {}
    if skill not in pool[name].keys():
        pool[name][skill] = 0
    if pool[name][skill] < value:
        pool[name][skill] = value
    return pool


def player_duel(player_1: str, player_2: str, pool: dict):
    player_1_total_strength = 0
    player_2_total_strength = 0
    for skill, value in pool[player_1].items():
        player_1_total_strength += value
    for skill, value in pool[player_2].items():
        player_2_total_strength += value

    for skill_player_1 in pool[player_1].values():
        if skill_player_1 in pool[player_2].values():
                if player_1_total_strength > player_2_total_strength:
                    pool[player_2].pop()
                elif player_1_total_strength < player_2_total_strength:
                    pool[player_1].pop()
    return pool

player_pool = {}

user_command = input()

while user_command != "Season end":

    if "->" in user_command:
        user_command = user_command.split("->")
        player_name = user_command[0].strip()
        player_skill = user_command[1].strip()
        player_strength = int(user_command[2].strip())
        player_pool = add_player(player_name, player_skill, player_strength, player_pool)
    elif "vs" in user_command:
        user_command = user_command.split("vs")
        first_name = user_command[0].strip()
        second_name = user_command[1].strip()
        player_pool = player_duel(first_name, second_name, player_pool)

    user_command = input()

print(player_pool)