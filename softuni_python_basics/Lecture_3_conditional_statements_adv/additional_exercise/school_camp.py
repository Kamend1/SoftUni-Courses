season = input()
type_group = input()
number_students = int(input())
number_nights = int(input())
type_sport = ""
price_stay = 0

if type_group == "boys" or type_group == "girls":
    if season == "Winter":
        price_stay = 9.60
    elif season == "Spring":
        price_stay = 7.20
    elif season == "Summer":
        price_stay = 15.00
elif type_group == "mixed":
    if season == "Winter":
        price_stay = 10.00
    elif season == "Spring":
        price_stay = 9.50
    elif season == "Summer":
        price_stay = 20

if season == "Winter":
    if type_group == "girls":
        type_sport = "Gymnastics"
    elif type_group == "boys":
        type_sport = "Judo"
    elif type_group == "mixed":
        type_sport = "Ski"
elif season == "Spring":
    if type_group == "girls":
        type_sport = "Athletics"
    elif type_group == "boys":
        type_sport = "Tennis"
    elif type_group == "mixed":
        type_sport = "Cycling"
elif season == "Summer":
    if type_group == "girls":
        type_sport = "Volleyball"
    elif type_group == "boys":
        type_sport = "Football"
    elif type_group == "mixed":
        type_sport = "Swimming"

amount_camp = price_stay * number_nights * number_students

if number_students >= 50:
    amount_camp *= 0.50
elif 20 <= number_students < 50:
    amount_camp *= 0.85
elif 10 <= number_students < 20:
    amount_camp *= 0.95

print(f"{type_sport} {amount_camp:.2f} lv.")
