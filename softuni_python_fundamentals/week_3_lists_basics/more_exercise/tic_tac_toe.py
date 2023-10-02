game = []

for i in range(3):
    game.append(list(int(x) for x in input().split()))

# first row
if game[0][0] == game[0][1] and game[0][2]:
    if game[0][0] == 1:
        print("First player won")
    elif game[0][0] == 2:
        print("Second player won")
    else:
        pass

# second row
elif game[1][0] == game[1][1] and game[1][2]:
    if game[1][0] == 1:
        print("First player won")
    elif game[1][0] == 2:
        print("Second player won")
    else:
        pass

# third row
elif game[2][0] == game[2][1] and game[2][2]:
    if game[2][0] == 1:
        print("First player won")
    elif game[2][0] == 2:
        print("Second player won")
    else:
        pass

# first column
elif game[0][0] == game[1][0] and game[2][0]:
    if game[0][0] == 1:
        print("First player won")
    elif game[0][0] == 2:
        print("Second player won")
    else:
        pass

# second column
elif game[0][1] == game[1][1] and game[2][1]:
    if game[0][1] == 1:
        print("First player won")
    elif game[0][1] == 2:
        print("Second player won")
    else:
        pass

# third column
elif game[0][2] == game[1][2] and game[2][2]:
    if game[0][2] == 1:
        print("First player won")
    elif game[0][2] == 2:
        print("Second player won")
    else:
        pass

# left diagonal
elif game[0][0] == game[1][1] and game[2][2]:
    if game[0][0] == 1:
        print("First player won")
    elif game[0][0] == 2:
        print("Second player won")
    else:
        pass

# right diagonal
elif game[0][2] == game[1][1] and game[2][0]:
    if game[0][2] == 1:
        print("First player won")
    elif game[0][2] == 2:
        print("Second player won")
    else:
        pass
else:
    print("Draw!")
