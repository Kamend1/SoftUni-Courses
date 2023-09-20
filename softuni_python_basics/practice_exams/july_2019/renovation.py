import sys
height_wall = int(input())
width_wall = int(input())
percent_unpainted = int(input())
total_area_to_paint = 4 * height_wall * width_wall * (1 - (percent_unpainted / 100))
area_painted = 0
liters_remaining = 0

for i in range(sys.maxsize):
    user_input_liters_or_command = input()
    if user_input_liters_or_command == "Tired!":
        break
    area_painted += int(user_input_liters_or_command)
    if area_painted >= total_area_to_paint:
        break

difference = abs(total_area_to_paint - area_painted)

if area_painted == total_area_to_paint:
    print("All walls are painted! Great job, Pesho!")
elif area_painted > total_area_to_paint:
    print(f"All walls are painted and you have {int(difference)} l paint left!")
else:
    print(f"{int(difference)} quadratic m left.")
