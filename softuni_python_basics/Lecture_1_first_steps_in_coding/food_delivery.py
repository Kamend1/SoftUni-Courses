qty_chicken_menu = int(input())
qty_fish_menu = int(input())
qty_veg_menu = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_veg_menu = 8.15
total_price_menu = qty_chicken_menu * price_chicken_menu \
                   + qty_fish_menu * price_fish_menu \
                   + qty_veg_menu * price_veg_menu
price_deset = 0.2 * total_price_menu
delivery_price = 2.50

total_order_price = total_price_menu + price_deset + delivery_price

print(total_order_price)
