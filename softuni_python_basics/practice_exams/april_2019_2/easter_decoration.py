price_basket = 1.50
price_wreath = 3.80
price_chocolate_bunny = 7
customer_total_amount = 0
customer_number_of_items = 0
all_total_amount = 0

number_customers = int(input())

for customer in range(number_customers):
    type_purchase = input()
    while type_purchase != "Finish":
        if type_purchase == "basket":
            customer_total_amount += price_basket
            customer_number_of_items += 1
        elif type_purchase == "wreath":
            customer_total_amount += price_wreath
            customer_number_of_items += 1
        elif type_purchase == "chocolate bunny":
            customer_total_amount += price_chocolate_bunny
            customer_number_of_items += 1
        type_purchase = input()

        if type_purchase == "Finish":
            if customer_number_of_items % 2 == 0:
                customer_total_amount *= 0.80
                all_total_amount += customer_total_amount
            else:
                all_total_amount += customer_total_amount
            print(F"You purchased {customer_number_of_items} items for {customer_total_amount:.2f} leva.")
            customer_total_amount = 0
            customer_number_of_items = 0


average_bill_customer = all_total_amount / number_customers
print(f"Average bill per client is: {average_bill_customer:.2f} leva.")
