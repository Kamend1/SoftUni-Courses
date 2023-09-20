type_fuel = str(input())
amount_fuel = int(input())

if type_fuel == "Diesel":
    if amount_fuel >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif type_fuel == "Gasoline":
    if amount_fuel >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif type_fuel == "Gas":
    if amount_fuel >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")
