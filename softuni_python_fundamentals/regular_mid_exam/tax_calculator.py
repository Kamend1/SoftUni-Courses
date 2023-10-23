vehicles_list = input().split(">>")
initial_family = 50
initial_heavyduty = 80
initial_sports = 100
total_tax = 0

for vehicle in vehicles_list:
    vehicle = vehicle.split()
    if vehicle[0] not in ["family", "heavyDuty", "sports"]:
        print("Invalid car type.")
    else:
        if vehicle[0] == "family":
            tax = 12 * (int(vehicle[2]) // 3000) + (initial_family - int(vehicle[1]) * 5)
            total_tax += tax
            print(f"A {vehicle[0]} car will pay {tax:.2f} euros in taxes.")
        elif vehicle[0] == "heavyDuty":
            tax = 14 * (int(vehicle[2]) // 9000) + (initial_heavyduty - int(vehicle[1]) * 8)
            total_tax += tax
            print(f"A {vehicle[0]} car will pay {tax:.2f} euros in taxes.")
        elif vehicle[0] == "sports":
            tax = 18 * (int(vehicle[2]) // 2000) + (initial_sports - int(vehicle[1]) * 9)
            total_tax += tax
            print(f"A {vehicle[0]} car will pay {tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
