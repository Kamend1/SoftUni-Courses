from collections import deque

values_bees = deque(int(x) for x in input().split())
values_nectar = [int(x) for x in input().split()]
honey_making_symbols = deque(x for x in input().split())
total_honey_made = 0

while values_bees and values_nectar:
    current_bee = values_bees.popleft()
    current_nectar = values_nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = honey_making_symbols.popleft()
        if current_symbol == "/":
            if current_nectar == 0:
                continue
            else:
                honey_made = abs(current_bee / current_nectar)
                total_honey_made += honey_made
        elif current_symbol == "*":
            honey_made = abs(current_bee * current_nectar)
            total_honey_made += honey_made
        elif current_symbol == "+":
            honey_made = abs(current_bee + current_nectar)
            total_honey_made += honey_made
        elif current_symbol == "-":
            honey_made = abs(current_bee - current_nectar)
            total_honey_made += honey_made
    else:
        values_bees.appendleft(current_bee)

print(f"Total honey made: {total_honey_made}")
if values_bees:
    print_str = ', '.join(str(x) for x in values_bees)
    print(f"Bees left: {print_str}")
if values_nectar:
    print_str = ', '.join(str(x) for x in values_nectar)
    print(f"Nectar left: {print_str}")
