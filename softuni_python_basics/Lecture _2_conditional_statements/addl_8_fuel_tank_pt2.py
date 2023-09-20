type_fuel = str(input())
quantity_fuel = float(input())
club_card = str(input())

gasoline_price = 2.22
gasoline_amount = gasoline_price * quantity_fuel
gasoline_price_card = gasoline_price - 0.18
gasoline_amount_card = gasoline_price_card * quantity_fuel
diesel_price = 2.33
diesel_amount = diesel_price * quantity_fuel
diesel_price_card = diesel_price - 0.12
diesel_amount_card = diesel_price_card * quantity_fuel
gas_price = 0.93
gas_amount = gas_price * quantity_fuel
gas_price_card = gas_price - 0.08
gas_amount_card = gas_price_card * quantity_fuel

if club_card == "Yes":
    if type_fuel == "Gasoline":
        if quantity_fuel > 25:
            gasoline_amount_card *= 0.90
            print(f"{gasoline_amount_card:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            gasoline_amount_card *= 0.92
            print(f"{gasoline_amount_card:.2f} lv.")
        else:
            print(f"{gasoline_amount_card:.2f} lv.")
    elif type_fuel == "Diesel":
        if quantity_fuel > 25:
            diesel_amount_card *= 0.90
            print(f"{diesel_amount_card:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            diesel_amount_card *= 0.92
            print(f"{diesel_amount_card:.2f} lv.")
        else:
            print(f"{diesel_amount_card:.2f} lv.")
    else:
        if quantity_fuel > 25:
            gas_amount_card *= 0.90
            print(f"{gas_amount_card:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            gas_amount_card *= 0.92
            print(f"{gas_amount_card:.2f} lv.")
        else:
            print(f"{gas_amount_card:.2f} lv.")
else:
    if type_fuel == "Gasoline":
        if quantity_fuel > 25:
            gasoline_amount *= 0.90
            print(f"{gasoline_amount:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            gasoline_amount *= 0.92
            print(f"{gasoline_amount:.2f} lv.")
        else:
            print(f"{gasoline_amount:.2f} lv.")
    elif type_fuel == "Diesel":
        if quantity_fuel > 25:
            diesel_amount *= 0.90
            print(f"{diesel_amount:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            diesel_amount *= 0.92
            print(f"{diesel_amount:.2f} lv.")
        else:
            print(f"{diesel_amount:.2f} lv.")
    else:
        if quantity_fuel > 25:
            gas_amount *= 0.90
            print(f"{gas_amount:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            gas_amount *= 0.92
            print(f"{gas_amount:.2f} lv.")
        else:
            print(f"{gas_amount:.2f} lv.")
