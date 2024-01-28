from collections import deque

monsters = deque(int(x) for x in input().split(','))
soldiers = [int(x) for x in input().split(',')]
monsters_killed = 0

while True:
    current_monster = monsters.popleft()
    current_soldier = soldiers.pop()

    if current_soldier > current_monster:
        current_soldier -= current_monster
        monsters_killed += 1

        if soldiers:
            soldiers[-1] += current_soldier
        else:
            soldiers.append(current_soldier)
    elif current_soldier == current_monster:
        monsters_killed += 1
    else:
        current_monster -= current_soldier
        monsters.append(current_monster)


    if not soldiers:
        break

    if not monsters:
        break

if not monsters:
    print("All monsters have been killed!")

if not soldiers:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
