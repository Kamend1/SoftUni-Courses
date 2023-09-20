name_airline = str(input())
number_adult_tickets = int(input())
number_child_tickers = int(input())
net_price_adult = float(input())
price_service = float(input())
net_price_child = 0.30 * net_price_adult

total_price = number_child_tickers * (net_price_child + price_service) \
              + number_adult_tickets * (net_price_adult + price_service)

profit_agency = 0.20 * total_price

print(f"The profit of your agency from {name_airline} tickets is {profit_agency:.2f} lv.")
