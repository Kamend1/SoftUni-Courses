number_places_sea = int(input())
number_places_mountain = int(input())
sold_out = False
price_sea = 680
price_mountain = 499
total_profit = 0

while True:
    user_input = input()
    if user_input == "Stop":
        break
    elif user_input == "sea":
        if number_places_sea > 0:
            number_places_sea -= 1
            total_profit += price_sea
        else:
            continue
    elif user_input == "mountain":
        if number_places_mountain > 0:
            number_places_mountain -= 1
            total_profit += price_mountain
    if number_places_mountain <= 0 and number_places_sea <= 0:
        sold_out = True
        break

if sold_out:
    print("Good job! Everything is sold.")
    print(f"Profit: {total_profit} leva.")
else:
    print(f"Profit: {total_profit} leva.")
