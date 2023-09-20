name_movie = str(input())
number_days = int(input())
number_tickets = int(input())
price_ticket = float(input())
percent_cinema = int(input())

profit = (number_tickets * number_days * price_ticket) * (1 - percent_cinema / 100)

print(f"The profit from the movie {name_movie} is {profit:.2f} lv.")
