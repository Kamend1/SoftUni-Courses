people_waiting = int(input())
state_lift_wagons = [int(x) for x in input().split()]

for idx in range(len(state_lift_wagons)):
    if state_lift_wagons[idx] < 4:
        if people_waiting >= 4 - state_lift_wagons[idx]:
            people_waiting -= 4 - state_lift_wagons[idx]
            state_lift_wagons[idx] = 4
        else:
            state_lift_wagons[idx] += people_waiting
            people_waiting = 0
            break

if people_waiting != 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
elif people_waiting == 0:
    if sum(state_lift_wagons) < len(state_lift_wagons) * 4:
        print("The lift has empty spots!")
print(*state_lift_wagons, sep=" ")
