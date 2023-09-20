needed_vacation_money = float(input())
available_money = float(input())
number_days_total = 0
number_days_spend = 0

while available_money < needed_vacation_money:
    type_action = input()

    if type_action == "spend":
        action_amount = float(input())
        if available_money <= action_amount:
            number_days_spend += 1
            number_days_total += 1
            available_money = 0
        else:
            available_money -= action_amount
            number_days_spend += 1
            number_days_total += 1
        if number_days_spend == 5:
            print(f"You can't save the money.")
            print(f"{number_days_total}")
            break

    elif type_action == "save":
        action_amount = float(input())
        difference = (needed_vacation_money - available_money)
        if difference >= action_amount:
            available_money += action_amount
            number_days_spend = 0
            number_days_total += 1
        else:
            number_days_total += 1
            print(f"You saved the money for {number_days_total} days.")
            break
else:
    print(f"You saved the money for {number_days_total} days.")
