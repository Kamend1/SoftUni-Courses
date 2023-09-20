screening_type = str(input())
number_rows = int(input())
number_columns = int(input())
price_premiere = 12.00
price_normal = 7.50
price_discount = 5.00

income = 0
cinema_capacity= number_columns * number_rows

if screening_type == "Premiere":
    income = cinema_capacity * price_premiere
elif screening_type == "Normal":
    income = cinema_capacity * price_normal
elif screening_type == "Discount":
    income = cinema_capacity * price_discount

print(f"{income:.2f} leva")
