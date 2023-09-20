age_lily = int(input())
price_washer = float(input())
price_toy = int(input())
saved_sum_toys = 0
saved_sum_money = 0
number_even = 0

for i in range(1, age_lily + 1):
    if i % 2 != 0:
        saved_sum_toys += price_toy
    elif i % 2 == 0:
        number_even += 1
        saved_sum_money += (10 * number_even) - 1

total_saved = saved_sum_money + saved_sum_toys
difference = abs(total_saved - price_washer)

if total_saved >= price_washer:
    print(f"Yes! {difference:.2f}" )
else:
    print(f"No! {difference:.2f}")
