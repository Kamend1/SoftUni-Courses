from collections import deque

food_qty = int(input())
customer_queue = [int(x) for x in input().split()]
customer_queue = deque(customer_queue)

print(max(customer_queue))

for _ in range(len(customer_queue)):
    if customer_queue[0] <= food_qty:
        food_qty -= customer_queue.popleft()
    else:
        break

if len(customer_queue) == 0:
    print("Orders complete")
else:
    new_string = "Orders left:"
    while customer_queue:
        new_string += " " + str(customer_queue.popleft())
    print(new_string)
