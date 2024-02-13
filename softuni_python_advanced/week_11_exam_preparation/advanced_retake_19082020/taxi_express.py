from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while True:
    if not taxis or not customers:
        break

    current_taxi = taxis[-1]
    current_customer = customers[0]

    if current_taxi >= current_customer:
        taxis.pop()
        customers.popleft()
        total_time += current_customer
    else:
        taxis.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
