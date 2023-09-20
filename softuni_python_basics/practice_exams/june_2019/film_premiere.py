movie_title = input()
type_package = input()
number_tickets = int(input())
price = 0

if movie_title == "John Wick":
    if type_package == "Drink":
        price = 12
    elif type_package == "Popcorn":
        price = 15
    elif type_package == "Menu":
        price = 19
elif movie_title == "Star Wars":
    if type_package == "Drink":
        price = 18
    elif type_package == "Popcorn":
        price = 25
    elif type_package == "Menu":
        price = 30
elif movie_title == "Jumanji":
    if type_package == "Drink":
        price = 9
    elif type_package == "Popcorn":
        price = 11
    elif type_package == "Menu":
        price = 14

if movie_title == "Star Wars" and number_tickets >= 4:
    price *= 0.70

if movie_title == "Jumanji" and number_tickets == 2:
    price *= 0.85

amount_paid = number_tickets * price
print(f"Your bill is {amount_paid:.2f} leva.")
