from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))
caffeine_intake = 0

while True:
    current_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()
    current_intake = current_caffeine * current_drink
    if 300 - caffeine_intake >= current_intake:
        caffeine_intake += current_intake
    else:
        energy_drinks.append(current_drink)
        caffeine_intake -= 30
        if caffeine_intake < 0:
            caffeine_intake = 0

    if not caffeine or not energy_drinks:
        break

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {caffeine_intake} mg caffeine.")
