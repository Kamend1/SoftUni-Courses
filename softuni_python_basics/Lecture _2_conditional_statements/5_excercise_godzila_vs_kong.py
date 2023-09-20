movie_budget = float(input())
number_statists = int(input())
price_clothing = float(input())
decor_movie = movie_budget * 0.10
amount_clothing = 0
total_expenses = 0
budget_left = 0

if number_statists >= 150:
    amount_clothing = number_statists * price_clothing * 0.9
    total_expenses = decor_movie + amount_clothing
else:
    amount_clothing = number_statists * price_clothing
    total_expenses = decor_movie + amount_clothing

if movie_budget - total_expenses >= 0:
    budget_left = movie_budget - total_expenses
    print('Action!')
    print(f'Wingard starts filming with {budget_left:.2f} leva left.')
else:
    budget_left = total_expenses - movie_budget
    print('Not enough money!')
    print(f'Wingard needs {budget_left:.2f} leva more.')
