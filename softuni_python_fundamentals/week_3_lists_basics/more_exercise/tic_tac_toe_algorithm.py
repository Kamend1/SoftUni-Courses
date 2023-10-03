def explore_matrix(matrix):
    possible_moves = []
    for row in matrix:
        for element in row:
            if element == 0:
                possible_moves.append(element)
            elif element != 0:
                check_for_winner(element)
    return possible_moves

def check_for_winner(player_symbol, matrix):
  # Check for a win in a row.
  for row in matrix:
    if all(element == player_symbol for element in row):
      return True

  # Check for a win in a column.
  for column in range(len(matrix[0])):
    if all(matrix[row][column] == player_symbol for row in range(len(matrix))):
      return True

  # Check for a win in a diagonal.
  if all(matrix[row][row] == player_symbol for row in range(len(matrix))):
    return True

  # Check for a win in the other diagonal.
  if all(matrix[row][len(matrix) - row - 1] == player_symbol for row in range(len(matrix))):
    return True

  # If no winner is found, return False.
  return False

game = []

for i in range(3):
    game.append(list(int(x) for x in input().split()))

if check_for_winner(1, game) == True:
    print("First player won")
elif check_for_winner(2, game) == True:
    print("Second player won")
else:
    print("Draw!")
