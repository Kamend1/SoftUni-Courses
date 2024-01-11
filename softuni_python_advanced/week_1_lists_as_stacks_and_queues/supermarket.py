from collections import deque

customer_queue = deque()

command = input()

while command != 'End':
    if command == 'Paid':
        if customer_queue:
            while customer_queue:
                print(customer_queue.popleft())
    else:
        customer_queue.append(command)
    command = input()

print(f"{len(customer_queue)} people remaining.")
