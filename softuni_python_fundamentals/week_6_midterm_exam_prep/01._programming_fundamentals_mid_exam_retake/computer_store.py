price_list = []

while True:
    user_command = input()
    if user_command == "special":
        if sum(price_list) > 0:
            print("Congratulations you've just bought a new computer!")
            price_before_taxes = sum(price_list)
            taxes = 0.2 * price_before_taxes
            final_price = (price_before_taxes + taxes) * 0.90
            print(f"Price without taxes: {price_before_taxes:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {final_price:.2f}$")
        else:
            print("Invalid order!")
        break
    elif user_command == "regular":
        if sum(price_list) > 0:
            print("Congratulations you've just bought a new computer!")
            price_before_taxes = sum(price_list)
            taxes = 0.2 * price_before_taxes
            final_price = price_before_taxes + taxes
            print(f"Price without taxes: {price_before_taxes:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {final_price:.2f}$")
        else:
            print("Invalid order!")
        break
    current_price = float(user_command)
    if current_price < 0:
        print("Invalid price!")
    else:
        price_list.append(current_price)
