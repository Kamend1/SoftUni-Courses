budget = float(input())
season = str(input())
destination = ""
type_lodging = ""
amount_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_lodging = "Camp"
        amount_spent = 0.30 * budget
    else:
        type_lodging = "Hotel"
        amount_spent = 0.70 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_lodging = "Camp"
        amount_spent = 0.40 * budget
    else:
        type_lodging = "Hotel"
        amount_spent = 0.80 * budget
elif budget > 1000:
    destination = "Europe"
    type_lodging = "Hotel"
    amount_spent = 0.90 * budget

print(f"Somewhere in {destination}")
print(f"{type_lodging} - {amount_spent:.2f}")
