capacity_stadium = int(input())
number_fans = int(input())

fans_in_a = 0
fans_in_b = 0
fans_in_v = 0
fans_in_g = 0
percent_full = number_fans * 100 / capacity_stadium

for fans in range(number_fans):
    fan_sector = input()
    if fan_sector == "A":
        fans_in_a += 1
    elif fan_sector == "B":
        fans_in_b += 1
    elif fan_sector == "V":
        fans_in_v += 1
    elif fan_sector == "G":
        fans_in_g += 1

percent_a = fans_in_a * 100 / number_fans
percent_b = fans_in_b * 100 / number_fans
percent_v = fans_in_v * 100 / number_fans
percent_g = fans_in_g * 100 / number_fans

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_full:.2f}%")
