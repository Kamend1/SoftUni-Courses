def team_lineup(*args):
    lineup = {}

    for arg in args:
        player, team = arg
        if team not in lineup:
            lineup[team] = []
        lineup[team].append(player)

    lineup = (sorted(lineup.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''
    for team_list in lineup:
        result += team_list[0] + ':' + '\n'
        for player in team_list[1]:
            result += '  -' + player + '\n'

    return result

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

