from collections import deque

cups_queue = deque(int(x) for x in input().split())
bottles_stack = [int(x) for x in input().split()]
wasted_water = 0

while cups_queue and bottles_stack:
    #draw a bottle from the back of the stack
    current_bottle = bottles_stack.pop()
    #check whether we have filled the cup, wasted water
    if cups_queue[0] <= current_bottle:
        current_cup = cups_queue.popleft()
        current_bottle -= current_cup
        wasted_water += current_bottle
    else:
        cups_queue[0] -= current_bottle

#print the required output
if cups_queue:
    string_to_print = f"Cups:"
    for _ in range(len(cups_queue)):
        string_to_print += f" {cups_queue.popleft()}"
    print(string_to_print)
else:
    string_to_print = f"Bottles:"
    for _ in range(len(bottles_stack)):
        string_to_print += f" {bottles_stack.pop()}"
    print(string_to_print)
print(f"Wasted litters of water: {wasted_water}")
