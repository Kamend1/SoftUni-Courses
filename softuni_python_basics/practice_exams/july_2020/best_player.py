user_command_input = input()
there_is_hattrick = False
best_player_name = ""
most_goals = 0

while user_command_input != "END":
    number_scored_goals = int(input())
    if number_scored_goals >= 3:
        there_is_hattrick = True
    if number_scored_goals >= 10:
        most_goals = number_scored_goals
        best_player_name = user_command_input
        there_is_hattrick = True
        break
    if number_scored_goals > most_goals:
        most_goals = number_scored_goals
        best_player_name = user_command_input
    user_command_input = input()

print(f"{best_player_name} is the best player!")
if there_is_hattrick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
