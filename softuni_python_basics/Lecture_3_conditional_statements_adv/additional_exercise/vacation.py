budget = float(input())
season = input()
price_stay = 0
location = ""
type_lodging = ""

if budget <= 1000:
    type_lodging = "Camp"
    if season == "Summer":
        location = "Alaska"
        price_stay = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price_stay = budget * 0.45
elif 1000 < budget <= 3000:
    type_lodging = "Hut"
    if season == "Summer":
        location = "Alaska"
        price_stay = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price_stay = budget * 0.60
elif budget > 3000:
    type_lodging = "Hotel"
    price_stay = budget * 0.90
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {type_lodging} - {price_stay:.2f}")
