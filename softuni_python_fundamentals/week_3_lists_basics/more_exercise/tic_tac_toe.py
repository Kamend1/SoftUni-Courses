game = []
game_is_draw = True

for i in range(3):
    game.append(list(int(x) for x in input().split()))

# first row
if game[0][0] == 1 and (game[0][0] == game[0][1] and game[0][2]):
    print("First player won")
    game_is_draw = False
elif game[0][0] == 2 and (game[0][0] == game[0][1] and game[0][2]):
    print("Second player won")
    game_is_draw = False

# second row
elif game[1][0] == 1 and (game[1][0] == game[1][1] and game[1][2]):
    print("First player won")
    game_is_draw = False
elif game[1][0] == 2 and (game[1][0] == game[1][1] and game[1][2]):
    print("Second player won")
    game_is_draw = False

# third row
elif game[0][0] == 1 and (game[2][0] == game[2][1] and game[2][2]):
    print("First player won")
    game_is_draw = False
elif game[0][0] == 2 and (game[2][0] == game[2][1] and game[2][2]):
    print("Second player won")
    game_is_draw = False

# first column
elif game[0][0] == 1 and (game[0][0] == game[1][0] and game[2][0]):
    print("First player won")
    game_is_draw = False
elif game[0][0] == 2 and (game[0][0] == game[1][0] and game[2][0]):
    print("Second player won")
    game_is_draw = False

# second column
elif game[0][1] == 1 and (game[0][1] == game[1][1] and game[2][1]):
    print("First player won")
    game_is_draw = False
elif game[0][1] == 2 and (game[0][1] == game[1][1] and game[2][1]):
    print("Second player won")
    game_is_draw = False

# third column
elif game[0][2] == 1 and (game[0][2] == game[1][2] and game[2][2]):
    print("First player won")
    game_is_draw = False
elif game[0][2] == 2 and (game[0][2] == game[1][2] and game[2][2]):
    print("Second player won")
    game_is_draw = False

# left diagonal
elif game[0][0] == 1 and (game[0][0] == game[1][1] and game[2][2]):
    print("First player won")
    game_is_draw = False
elif game[0][0] == 2 and (game[0][0] == game[1][1] and game[2][2]):
    print("Second player won")
    game_is_draw = False

# right diagonal
elif game[0][2] == 1 and (game[0][2] == game[1][1] and game[2][0]):
    print("First player won")
    game_is_draw = False
elif game[0][2] == 2 and (game[0][2] == game[1][1] and game[2][0]):
    print("Second player won")
    game_is_draw = False

if game_is_draw:
    print("Draw!")
