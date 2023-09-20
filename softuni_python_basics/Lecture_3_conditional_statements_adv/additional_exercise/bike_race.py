number_junior = int(input())
number_senior = int(input())
type_trail = str(input())
entrance_fee_junior = 0
entrance_fee_senior = 0

if type_trail == "trail":
    entrance_fee_junior = 5.50
    entrance_fee_senior = 7
elif type_trail == "cross-country":
    if number_junior + number_senior >= 50:
        entrance_fee_junior = 8 * 0.75
        entrance_fee_senior = 9.50 * 0.75
    else:
        entrance_fee_junior = 8
        entrance_fee_senior = 9.50
elif type_trail == "downhill":
    entrance_fee_junior = 12.25
    entrance_fee_senior = 13.75
elif type_trail == "road":
    entrance_fee_junior = 20
    entrance_fee_senior = 21.50

amount_collected = entrance_fee_senior * number_senior + entrance_fee_junior * number_junior
amount_given = amount_collected * 0.95

print(f"{amount_given:.2f}")
