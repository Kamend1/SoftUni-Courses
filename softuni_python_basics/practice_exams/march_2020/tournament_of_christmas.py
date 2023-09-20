number_days_tournament = int(input())
number_games_won = 0
number_games_lost = 0
amount_won_day = 0
days_won = 0
amount_won = 0
tournament_won = False

for day in range(number_days_tournament):
    sport_type = input()
    while sport_type != "Finish":
        play_outcome = input()
        if play_outcome == "win":
            number_games_won += 1
            amount_won_day += 20
        if play_outcome == "lose":
            number_games_lost += 1
        sport_type = input()
        if sport_type == "Finish":
            if number_games_won > number_games_lost:
                amount_won_day *= 1.10
                days_won += 1
            else:
                days_won -= 1
            number_games_won = 0
            number_games_lost = 0
    amount_won += amount_won_day
    amount_won_day = 0

if days_won > 0:
    tournament_won = True
    amount_won *= 1.20

if tournament_won:
    print(f"You won the tournament! Total raised money: {amount_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {amount_won:.2f}")
