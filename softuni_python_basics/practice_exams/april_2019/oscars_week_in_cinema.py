name_movie = input()
type_hall = input()
number_tickets = int(input())
price_seat = 0

if name_movie == "A Star Is Born":
    if type_hall == "normal":
        price_seat = 7.50
    elif type_hall == "luxury":
        price_seat = 10.50
    elif type_hall == "ultra luxury":
        price_seat = 13.50
elif name_movie == "Bohemian Rhapsody":
    if type_hall == "normal":
        price_seat = 7.35
    elif type_hall == "luxury":
        price_seat = 9.45
    elif type_hall == "ultra luxury":
        price_seat = 12.75
elif name_movie == "Green Book":
    if type_hall == "normal":
        price_seat = 8.15
    elif type_hall == "luxury":
        price_seat = 10.25
    elif type_hall == "ultra luxury":
        price_seat = 13.25
elif name_movie == "The Favourite":
    if type_hall == "normal":
        price_seat = 8.75
    elif type_hall == "luxury":
        price_seat = 11.55
    elif type_hall == "ultra luxury":
        price_seat = 13.95

income_movie = number_tickets * price_seat
print(f"{name_movie} -> {income_movie:.2f} lv.")
