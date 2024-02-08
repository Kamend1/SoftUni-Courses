from collections import deque

firework_effects = deque([int(x) for x in input().split(', ') if int(x) > 0])
explosive_power = [int(x) for x in input().split(', ') if int(x) > 0]


firework_types = {'Palm': 0, 'Willow': 0, 'Crossette': 0}
firework_success = False

while True:
    if not firework_effects or not explosive_power:
        break

    current_effect = firework_effects.popleft()
    current_power = explosive_power.pop()

    result = current_effect + current_power

    if result % 3 == 0 and result % 5 != 0:
        firework_types['Palm'] += 1
    elif result % 3 != 0 and result % 5 == 0:
        firework_types['Willow'] += 1
    elif result % 15 == 0:
        firework_types['Crossette'] += 1
    else:
        if current_effect >= 2:
            firework_effects.append(current_effect - 1)
        explosive_power.append(current_power)

    if firework_types['Palm'] >= 3 and firework_types['Willow'] >= 3 and firework_types['Crossette'] >= 3:
        firework_success = True
        break

if firework_success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for k, v in firework_types.items():
    print(f"{k} Fireworks: {v}")
