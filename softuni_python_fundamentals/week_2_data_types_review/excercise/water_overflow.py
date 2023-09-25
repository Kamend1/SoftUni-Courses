num_lines = int(input())
water_poured = 0

for i in range(num_lines):
    line_liters = int(input())
    if (255 - water_poured) < line_liters:
        print("Insufficient capacity!")
        continue
    water_poured += line_liters

print(water_poured)
