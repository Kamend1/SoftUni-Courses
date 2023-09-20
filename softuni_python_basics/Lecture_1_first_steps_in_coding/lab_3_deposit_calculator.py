deposit_amount = float(input())
term_months = int(input())
annual_int_rate = float(input())
interest_amount = deposit_amount * term_months * (annual_int_rate / (12*100))
amount_end = deposit_amount + interest_amount

print(amount_end)
