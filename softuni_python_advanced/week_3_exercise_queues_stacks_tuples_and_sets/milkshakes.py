from collections import deque

chocolates_stack = [int(x) for x in input().split(', ')]
cups_milk_queue = deque(int(x) for x in input().split(', '))
milkshakes_made = 0
enough_milkshakes = False

while chocolates_stack and cups_milk_queue:
    current_chocolate = chocolates_stack.pop()
    current_milk = cups_milk_queue.popleft()
    if current_chocolate <= 0:
        if current_milk > 0:
            cups_milk_queue.appendleft(current_milk)
            continue
        else:
            continue
    if current_milk <= 0:
        if current_chocolate > 0:
            chocolates_stack.append(current_chocolate)
            continue
        else:
            continue
    if current_chocolate == current_milk:
        milkshakes_made += 1
        if milkshakes_made == 5:
            enough_milkshakes = True
            print("Great! You made all the chocolate milkshakes needed!")
            break
    else:
        current_chocolate -= 5
        if current_chocolate > 0:
            chocolates_stack.append(current_chocolate)
        cups_milk_queue.append(current_milk)
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    news_str = ', '.join(str(x) for x in chocolates_stack)
    print(f"Chocolate: {news_str}")
else:
    print("Chocolate: empty")
if cups_milk_queue:
    news_str = ', '.join(str(x) for x in cups_milk_queue)
    print(f"Milk: {news_str}")
else:
    print("Milk: empty")
