number_of_kozunak = int(input())

baker_total_points = 0
max_points = 0
baker_max_name = ""

for i in range(number_of_kozunak):
    name_of_baker = input()
    current_score = input()
    while current_score != "Stop":
        baker_total_points += int(current_score)
        current_score = input()
    print(f"{name_of_baker} has {baker_total_points} points.")
    if baker_total_points > max_points:
        max_points = baker_total_points
        baker_max_name = name_of_baker
        print(f"{name_of_baker} is the new number 1!")
    baker_total_points = 0

print(f"{baker_max_name} won competition with {max_points} points!")
