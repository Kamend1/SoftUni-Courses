from collections import deque

kids_names = input().split()
kids_queue = deque()
for name in kids_names:
    kids_queue.append(name)

num_toss = int(input())
toss_counter = 0

while len(kids_queue) > 1:
    toss_counter += 1
    if toss_counter == num_toss:
        print(f"Removed {kids_queue.popleft()}")
        toss_counter = 0
    else:
        kids_queue.rotate(-1)

print(f"Last is {kids_queue.popleft()}")
