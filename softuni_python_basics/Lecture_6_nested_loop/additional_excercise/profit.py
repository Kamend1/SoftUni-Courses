coins_one_lv = int(input())
coins_two_lv = int(input())
banknotes_five_lv = int(input())
total_amount = int(input())

for num_one_lv in range(coins_one_lv + 1):
    for num_two_lv in range(coins_two_lv + 1):
        for num_five_lv in range(banknotes_five_lv + 1):
            amount_paid = num_one_lv + 2 * num_two_lv + 5 * num_five_lv
            if amount_paid == total_amount:
                print(f"{num_one_lv} * 1 lv. + {num_two_lv} * 2 lv. + {num_five_lv} * 5 lv. = {total_amount} lv.")
