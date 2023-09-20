first_game_result = input()
second_game_result = input()
third_game_result = input()

number_wins = 0
number_losses = 0
number_draws = 0

if int(first_game_result[0]) > int(first_game_result[2]):
    number_wins += 1
elif int(first_game_result[0]) == int(first_game_result[2]):
    number_draws += 1
elif int(first_game_result[0]) < int(first_game_result[2]):
    number_losses += 1

if int(second_game_result[0]) > int(second_game_result[2]):
    number_wins += 1
elif int(second_game_result[0]) == int(second_game_result[2]):
    number_draws += 1
elif int(second_game_result[0]) < int(second_game_result[2]):
    number_losses += 1

if int(third_game_result[0]) > int(third_game_result[2]):
    number_wins += 1
elif int(third_game_result[0]) == int(third_game_result[2]):
    number_draws += 1
elif int(third_game_result[0]) < int(third_game_result[2]):
    number_losses += 1

print(f"Team won {number_wins} games.")
print(f"Team lost {number_losses} games.")
print(f"Drawn games: {number_draws}")
