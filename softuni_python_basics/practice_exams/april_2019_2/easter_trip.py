destination = input()
time_travel = input()
number_nights = int(input())
price_night = 0

if destination == "France":
    if time_travel == "21-23":
        price_night = 30
    elif time_travel == "24-27":
        price_night = 35
    elif time_travel == "28-31":
        price_night = 40
elif destination == 'Italy':
    if time_travel == "21-23":
        price_night = 28
    elif time_travel == "24-27":
        price_night = 32
    elif time_travel == "28-31":
        price_night = 39
elif destination == "Germany":
    if time_travel == "21-23":
        price_night = 32
    elif time_travel == "24-27":
        price_night = 37
    elif time_travel == "28-31":
        price_night = 43

amount_spent = price_night * number_nights

print(f"Easter trip to {destination} : {amount_spent:.2f} leva.")

