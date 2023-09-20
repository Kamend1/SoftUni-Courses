number_sold_games = int(input())
number_hearthstone = 0
number_fornite = 0
number_overwatch = 0
number_others = 0

for i in range (number_sold_games):
    name_game_sold = input()
    if name_game_sold == "Hearthstone":
        number_hearthstone += 1
    elif name_game_sold == "Fornite":
        number_fornite += 1
    elif name_game_sold == "Overwatch":
        number_overwatch += 1
    else:
        number_others += 1

average_hearthstone = number_hearthstone * 100 / number_sold_games
average_fornite = number_fornite * 100 / number_sold_games
average_overwatch = number_overwatch * 100 / number_sold_games
average_others = number_others * 100 / number_sold_games

print(f"Hearthstone - {average_hearthstone:.2f}%")
print(f"Fornite - {average_fornite:.2f}%")
print(f"Overwatch - {average_overwatch:.2f}%")
print(f"Others - {average_others:.2f}%")
