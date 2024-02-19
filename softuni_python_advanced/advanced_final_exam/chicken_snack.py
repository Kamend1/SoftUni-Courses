from collections import deque

amount_of_money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])
food_count = 0

while True:
    if not amount_of_money or not prices:
        break

    current_amount = amount_of_money[-1]
    current_price = prices[0]

    if current_amount == current_price:
        amount_of_money.pop()
        prices.popleft()
        food_count += 1
    elif current_amount > current_price:
        difference = current_amount - current_price
        amount_of_money.pop()
        prices.popleft()
        if amount_of_money:
            amount_of_money[-1] += difference
        food_count += 1
    elif current_amount < current_price:
        amount_of_money.pop()
        prices.popleft()

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
elif food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {food_count} foods.")
