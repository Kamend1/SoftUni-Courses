from sys import maxsize
movie_budget = float(input())
amount_spent = 0
budget_left = movie_budget

for actor in range(maxsize):
    actor_name = input()
    if actor_name == "ACTION":
        print(f"We are left with {budget_left:.2f} leva.")
        break
    if len(actor_name) <= 15:
        price_actor = float(input())
        if price_actor > budget_left:
            print(f"We need {price_actor - budget_left:.2f} leva for our actors.")
            break
        else:
            budget_left -= price_actor
    elif len(actor_name) > 15:
        price_actor = 0.20 * budget_left
        if price_actor > budget_left:
            print(f"We need {price_actor - budget_left:.2f} leva for our actors.")
            break
        else:
            budget_left -= price_actor
