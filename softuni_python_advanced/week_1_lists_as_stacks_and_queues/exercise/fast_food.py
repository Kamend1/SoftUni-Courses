from collections import deque

food_qty = int(input())
customer_queue = deque(int(x) for x in input().split())

print(max(customer_queue))

for _ in range(len(customer_queue)):
    if customer_queue[0] <= food_qty:
        food_qty -= customer_queue.popleft()
    else:
        print("Orders left:", *customer_queue)
        break
else:
    print("Orders complete")
