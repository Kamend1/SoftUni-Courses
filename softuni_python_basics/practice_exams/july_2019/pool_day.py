from math import ceil

number_people = int(input())
entrance_fee = float(input())
price_sunbed = float(input())
price_umbrella = float(input())
number_sunbeds = ceil(number_people * 0.75)
number_umbrellas = ceil(number_people /2)

money_needed = number_sunbeds * price_sunbed \
               + number_umbrellas * price_umbrella \
               + entrance_fee * number_people

print(f"{money_needed:.2f} lv.")
