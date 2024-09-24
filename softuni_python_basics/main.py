needed_income = int(input())

price = 0

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        print(f"We need {abs(price - needed_income):.2f} leva more.")
        break

    number_cocktails = int(input())
    current_price = len(cocktail_name) * number_cocktails

    if current_price % 2 == 1:
        current_price *= 0.75

    price += current_price

    if price >= needed_income:
        print("Target acquired.")
        break

print(f"Club income - {price:.2f} leva.")

