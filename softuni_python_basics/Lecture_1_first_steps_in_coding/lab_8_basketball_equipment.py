annual_fee_basketball = int(input())

basket_shoes = annual_fee_basketball * (1 - 0.4)
basket_equip = basket_shoes * (1 - 0.2)
basket_ball = basket_equip * 0.25
basket_accessory = basket_ball * 0.20

total_cost = annual_fee_basketball + basket_shoes \
             + basket_equip + basket_ball \
             + basket_accessory

print(total_cost)
