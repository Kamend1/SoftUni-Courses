name_team = input()
number_games_played = int(input())
number_w = 0
number_d = 0
number_l = 0
points_won = 0
percentage_win_games = 0


if number_games_played == 0:
    print(f"{name_team} hasn't played any games during this season.")

for i in range(number_games_played):
    input_game_outcome = input()
    if input_game_outcome == "W":
        number_w += 1
        points_won += 3
    elif input_game_outcome == "D":
        number_d += 1
        points_won += 1
    elif input_game_outcome == "L":
        number_l += 1

if number_games_played != 0:
    percentage_win_games = number_w * 100 / number_games_played
    print(f"{name_team} has won {points_won} points during this season.")
    print("Total stats:")
    print(f"## W: {number_w}")
    print(f"## D: {number_d}")
    print(f"## L: {number_l}")
    print(f"Win rate: {percentage_win_games:.2f}%")
