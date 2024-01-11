from collections import deque

price_bullet = int(input())
size_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_intelligence = int(input())
total_value_bullets = 0

barrel = deque()

#load the gun for the first time
if len(bullets) >= size_gun_barrel:
    for _ in range(size_gun_barrel):
        barrel.append(bullets.pop())
else:
    if 0 < len(bullets) < size_gun_barrel:
        for _ in range(len(bullets)):
            barrel.append(bullets.pop())
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        exit()

while locks:
    #fire the gun
    current_bullet = barrel.popleft()
    total_value_bullets += price_bullet

    #checks whether we opened the lock or not
    if locks[0] >= current_bullet:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    #checks if the gun is still loaded
    if not barrel:
        if len(bullets) >= size_gun_barrel:
            for _ in range(size_gun_barrel):
                barrel.append(bullets.pop())
            print("Reloading!")
        else:
            if 0 < len(bullets) < size_gun_barrel:
                for _ in range(len(bullets)):
                    barrel.append(bullets.pop())
                print("Reloading!")
            else:
                break
    if not locks:
        break

#if the while loop is over, we check whether safe was open or not
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = value_intelligence - total_value_bullets
    print(f'{len(bullets) + len(barrel)} bullets left. Earned ${earned_money}')
