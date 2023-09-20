name_first_player = input()
name_second_player = input()
total_points_first_player = 0
total_points_second_player = 0

for cards in range(18):
    card_first_player_or_command = input()
    if card_first_player_or_command == "End of game":
        print(f"{name_first_player} has {total_points_first_player} points")
        print(f"{name_second_player} has {total_points_second_player} points")
        break
    card_second_player = int(input())
    if int(card_first_player_or_command) == card_second_player:
        second_card_first_player = int(input())
        second_card_second_player = int(input())
        if second_card_first_player > second_card_second_player:
            print("Number wars!")
            print(f"{name_first_player} is winner with {total_points_first_player} points")
            break
        elif second_card_first_player < second_card_second_player:
            print("Number wars!")
            print(f"{name_second_player} is winner with {total_points_second_player} points")
            break
    elif int(card_first_player_or_command) > card_second_player:
        total_points_first_player += int(card_first_player_or_command) - card_second_player
    elif int(card_first_player_or_command) < card_second_player:
        total_points_second_player += card_second_player - int(card_first_player_or_command)
