from collections import deque

num_petrol_pumps = int(input())
pump_queue = []
visited_queue = []
gas_tank = 0
start_index = 0

for _ in range(num_petrol_pumps):
    pump_data = [int(x) for x in input().split()]
    pump_queue.append(pump_data)

pump_queue = deque(pump_queue)

while pump_queue:
    current_pump = pump_queue.popleft()
    visited_queue.append(current_pump)
    gas_tank += current_pump[0]
    if gas_tank >= current_pump[1]:
        gas_tank -= current_pump[1]
    else:
        for pump in visited_queue:
            pump_queue.append(pump)
        start_index += len(visited_queue)
        gas_tank = 0
        visited_queue = []

print(start_index)
