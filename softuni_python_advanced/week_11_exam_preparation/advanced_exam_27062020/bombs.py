from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

bomb_dict = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

all_bombs = False

while True:
    if not bomb_effects or not bomb_casings:
        break

    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]

    if current_effect + current_casing == 40:
        bomb_dict['Datura Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_effect + current_casing == 60:
        bomb_dict['Cherry Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_effect + current_casing == 120:
        bomb_dict['Smoke Decoy Bombs'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if bomb_dict['Smoke Decoy Bombs'] >= 3 and bomb_dict['Cherry Bombs'] >= 3 and bomb_dict['Datura Bombs'] >= 3:
        all_bombs = True
        break

if all_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

for k, v in sorted(bomb_dict.items()):
    print(f"{k}: {v}")
