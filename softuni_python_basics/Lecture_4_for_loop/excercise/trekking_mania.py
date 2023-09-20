number_groups = int(input())
number_musala = 0
number_monblan = 0
number_kiliman = 0
number_k2 = 0
number_everest = 0
total_climbers = 0

for i in range(0, number_groups):
    group_size = int(input())
    if group_size <= 5:
        number_musala += group_size
        total_climbers += group_size
    elif 5 < group_size <= 12:
        number_monblan += group_size
        total_climbers += group_size
    elif 12 < group_size <= 25:
        number_kiliman += group_size
        total_climbers += group_size
    elif 25 < group_size <= 40:
        number_k2 += group_size
        total_climbers += group_size
    elif group_size >= 41:
        number_everest += group_size
        total_climbers += group_size

print(f"{number_musala * 100 / total_climbers:.2f}%")
print(f"{number_monblan * 100 / total_climbers:.2f}%")
print(f"{number_kiliman * 100 / total_climbers:.2f}%")
print(f"{number_k2 * 100 / total_climbers:.2f}%")
print(f"{number_everest * 100 / total_climbers:.2f}%")
