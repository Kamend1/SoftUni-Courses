command = input()

score = 0
biggest_score = 0
winner_name = ""

while command != "Stop":
    player_name = command
    for i in range(len(player_name)):
        number = int(input())
        if number == ord(command[i]):
            score += 10
        else:
            score += 2

    if score >= biggest_score:
        biggest_score = score
        winner_name = player_name
    score = 0

    command = input()

print(f"The winner is {winner_name} with {biggest_score} points!")
