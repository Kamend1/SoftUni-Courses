championship_stage = input()
type_ticket = input()
number_tickets = int(input())
picture_trophy = input()
price_ticket = 0

if championship_stage == "Quarter final":
    if type_ticket == "Standard":
        price_ticket = 55.50
    elif type_ticket == "Premium":
        price_ticket = 105.20
    elif type_ticket == "VIP":
        price_ticket = 118.90
elif championship_stage == "Semi final":
    if type_ticket == "Standard":
        price_ticket = 75.88
    elif type_ticket == "Premium":
        price_ticket = 125.22
    elif type_ticket == "VIP":
        price_ticket = 300.40
elif championship_stage == "Final":
    if type_ticket == "Standard":
        price_ticket = 110.10
    elif type_ticket == "Premium":
        price_ticket = 160.66
    elif type_ticket == "VIP":
        price_ticket = 400

amount_tickets = number_tickets * price_ticket
total_amount_spent = 0

if amount_tickets > 4000:
    total_amount_spent = amount_tickets * 0.75
elif 2500 <= amount_tickets < 4000 and picture_trophy == "Y":
    total_amount_spent = amount_tickets * 0.90 + number_tickets * 40
elif 2500 <= amount_tickets <= 4000 and picture_trophy == "N":
    total_amount_spent = amount_tickets * 0.90
elif amount_tickets < 2500 and picture_trophy == "Y":
    total_amount_spent = amount_tickets + number_tickets * 40
else:
    total_amount_spent = amount_tickets

print(f"{total_amount_spent:.2f}")
