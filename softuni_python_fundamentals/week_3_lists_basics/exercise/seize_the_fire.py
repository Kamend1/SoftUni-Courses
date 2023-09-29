cell_list = list(input().split("#"))
water = int(input())
effort = 0
total_fire = 0
cell_type = []
cell_value = []
cell_put_out = []
water_finished = False

for idx in range(len(cell_list)):
    cell_type.append(cell_list[idx].split(" ")[0])
    cell_value.append(int(cell_list[idx].split(" ")[2]))
    if cell_type[idx] == "High" and 81 <= cell_value[idx] <= 125:
        if int(cell_value[idx]) > water:
            continue
        water -= cell_value[idx]
        effort += cell_value[idx] * 0.25
        total_fire += cell_value[idx]
        cell_put_out.append(cell_value[idx])
    if cell_type[idx] == "Medium" and 51 <= cell_value[idx] <= 80:
        if int(cell_value[idx]) > water:
            continue
        water -= cell_value[idx]
        effort += cell_value[idx] * 0.25
        total_fire += cell_value[idx]
        cell_put_out.append(cell_value[idx])
    if cell_type[idx] == "Low" and 1 <= cell_value[idx] <= 50:
        if int(cell_value[idx]) > water:
            continue
        water -= cell_value[idx]
        effort += cell_value[idx] * 0.25
        total_fire += cell_value[idx]
        cell_put_out.append(cell_value[idx])
print("Cells:")
for cell in cell_put_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
