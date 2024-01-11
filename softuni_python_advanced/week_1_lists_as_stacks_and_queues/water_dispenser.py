from collections import deque

water_qty = int(input())
water_queue = deque()

name = input()
while name != 'Start':
    water_queue.append(name)
    name = input()

command = input()
while command != 'End':
    orders = command.split()
    if len(orders) == 1:
        if int(orders[0]) <= water_qty:
            print(f"{water_queue.popleft()} got water")
            water_qty -= int(orders[0])
        else:
            print(f"{water_queue.popleft()} must wait")
    else:
        water_qty += int(orders[1])
    command = input()

print(f"{water_qty} liters left")
