user_command = input()
current_index = 0
current_points = 0
max_points = 0
player_max_points = ""

while user_command != "Stop":
    name_player = user_command
    for character in name_player:
        player_number_input = int(input())
        if player_number_input == ord(character):
            current_points += 10
        else:
            current_points += 2
    if current_points >= max_points:
        max_points = current_points
        player_max_points = name_player
    current_points = 0
    user_command = input()

print(f"The winner is {player_max_points} with {max_points} points!")
