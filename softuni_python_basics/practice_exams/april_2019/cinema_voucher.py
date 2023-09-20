import sys
voucher_amount = int(input())
number_tickets_bought = 0
number_other_items = 0
amount_spent = 0
difference = (voucher_amount - amount_spent)

for i in range(sys.maxsize):
    user_input_purchase = input()
    if user_input_purchase == "End":
        break
    if len(user_input_purchase) > 8:
        price_item = ord(user_input_purchase[0]) + ord(user_input_purchase[1])
        if price_item > difference:
            break
        else:
            number_tickets_bought += 1
            amount_spent += price_item
    else:
        price_item = ord(user_input_purchase[0])
        if price_item > difference:
            break
        else:
            number_other_items += 1
            amount_spent += price_item

    difference = abs(voucher_amount - amount_spent)

print(int(number_tickets_bought))
print(int(number_other_items))
