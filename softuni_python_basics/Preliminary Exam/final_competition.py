number_dancers = int(input())
number_points = float(input())
season = input()
place = input()
total_money_earned = 0
amount_charity = 0

if place == "Bulgaria":
    total_money_earned = number_dancers * number_points
    if season == "summer":
        total_money_earned *= 0.95
    elif season == "winter":
        total_money_earned *= 0.92
elif place == "Abroad":
    total_money_earned = 1.5 * number_dancers * number_points
    if season == "summer":
        total_money_earned *= 0.90
    elif season == "winter":
        total_money_earned *= 0.85

amount_charity = 0.75 * total_money_earned
total_money_earned -= amount_charity
amount_per_dancer = total_money_earned / number_dancers

print(f"Charity - {amount_charity:.2f}")
print(f"Money per dancer - {amount_per_dancer:.2f}")
