number_orders = int(input())
total_price = 0

for i in range(number_orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        price_order = price * days * capsules
        print(f"The price for the coffee is: ${price_order:.2f}")
        total_price += price_order
    else:
        continue
print(f"Total: ${total_price:.2f}")
