team_a = 11
team_b = 11

cards = [str(string) for string in input().split()]
cards_checked = []
game_terminated = False

for card in cards:
    if card in cards_checked:
        continue
    if card[0] == "A":
        team_a -= 1
    elif card[0] == "B":
        team_b -= 1
    elif card == "":
        continue
    cards_checked.append(card)
    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")
