def add_player(name: str, skill: str, value: int, pool: dict):
    if name not in pool.keys():
        pool[name] = {}
    if skill not in pool[name].keys():
        pool[name][skill] = 0
    if pool[name][skill] < value:
        pool[name][skill] = value
    return pool


def player_duel(player_1: str, player_2: str, pool: dict):
    if player_1 in pool and player_2 in pool:
        to_remove = []
        for skill, value in pool[player_1].items():
            if skill in pool[player_2]:
                if pool[player_1][skill] > pool[player_2][skill]:
                    to_remove.append(player_2)
                elif pool[player_1][skill] < pool[player_2][skill]:
                    to_remove.append(player_1)

        for player in to_remove:
            pool.pop(player)

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

player_total_skill = {}

for key, value in player_pool.items():
    skill_sum = 0
    for skill, skill_score in value.items():
        skill_sum += skill_score
    if key not in player_total_skill:
        player_total_skill[key] = {}
    player_total_skill[key]['total skill'] = skill_sum


sorted_total_skill = dict(sorted(player_total_skill.items(), key=lambda x: (x[1]['total skill'], x[0]), reverse=True))

for key, value in player_pool.items():
    player_pool[key] = sorted(player_pool[key].items(), key=lambda x: (-x[1], x[0]))

for player, skill in sorted_total_skill.items():
    print(f"{player}: {skill['total skill']} skill")
    for skill_name, skill_value in player_pool[player]:
        print(f'- {skill_name} <::> {skill_value}')
