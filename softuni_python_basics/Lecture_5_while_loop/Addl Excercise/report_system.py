expected_sale_amount = int(input())
user_command_input = input()
is_amount_enough = False
cycle_counter = 0
amount_paid_cash = 0
amount_paid_card = 0
number_payments_cash = 0
number_payments_card = 0

while user_command_input != "End":
    cycle_counter += 1
    current_sum = int(user_command_input)
    if cycle_counter % 2 == 0 and not(current_sum < 10):
        print("Product sold!")
        amount_paid_card += current_sum
        expected_sale_amount -= current_sum
        number_payments_card += 1
    elif cycle_counter % 2 != 0 and not(current_sum > 100):
        print("Product sold!")
        amount_paid_cash += current_sum
        expected_sale_amount -= current_sum
        number_payments_cash += 1
    else:
        print("Error in transaction!")
    if expected_sale_amount <= 0:
        is_amount_enough = True
        break
    user_command_input = input()

if number_payments_card != 0:
    average_cc = amount_paid_card / number_payments_card
else:
    average_cc = 0
if number_payments_cash != 0:
    average_cs = amount_paid_cash / number_payments_cash
else:
    average_cs = 0

if is_amount_enough:
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
