square_meeters_for_work = float(input())
price_for_greening_yard = square_meeters_for_work * 7.61
discount = price_for_greening_yard * 0.18
final_price = price_for_greening_yard - discount

print(f"The final price is: {final_price}")
print(f"The discount is: {discount}")