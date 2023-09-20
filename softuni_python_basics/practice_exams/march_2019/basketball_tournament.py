name_of_tournament = input()
games_won = 0
games_lost = 0
total_games = 0

while name_of_tournament != "End of tournaments":
    number_games = int(input())
    for i in range(1, number_games + 1):
        desi_score = int(input())
        opponent_score = int(input())
        total_games += 1
        if desi_score > opponent_score:
            games_won += 1
            difference = abs(desi_score - opponent_score)
            print(f"Game {i} of tournament {name_of_tournament}: win with {difference} points.")
        elif desi_score < opponent_score:
            games_lost += 1
            difference = abs(desi_score - opponent_score)
            print(f"Game {i} of tournament {name_of_tournament}: lost with {difference} points.")
    name_of_tournament = input()

percent_won = games_won * 100 / total_games
percent_lost = games_lost * 100 / total_games

print(f"{percent_won:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")
