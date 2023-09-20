import sys

number_colored_eggs = int(input())
number_green = 0
number_red = 0
number_orange = 0
number_blue = 0
max_number = -sys.maxsize
max_color = ""

for i in range(number_colored_eggs):
    current_egg_color = input()
    if current_egg_color == "red":
        number_red += 1
        if number_red > max_number:
            max_number = number_red
            max_color = "red"
    elif current_egg_color == "orange":
        number_orange += 1
        if number_orange > max_number:
            max_number = number_orange
            max_color = "orange"
    elif current_egg_color == "green":
        number_green += 1
        if number_green > max_number:
            max_number = number_green
            max_color = "green"
    elif current_egg_color == "blue":
        number_blue += 1
        if number_blue > max_number:
            max_number = number_blue
            max_color = "blue"

print(f"Red eggs: {number_red}")
print(f"Orange eggs: {number_orange}")
print(f"Blue eggs: {number_blue}")
print(f"Green eggs: {number_green}")
print(f"Max eggs: {max_number} -> {max_color}")
