from collections import deque

egg_sizes = deque(int(x) for x in input().split(', '))
paper_sizes = deque(int(x) for x in input().split(', '))
boxes_filled = 0

while True:
    current_egg = egg_sizes.popleft()
    current_paper = paper_sizes.pop()

    if current_egg <= 0:
        paper_sizes.append(current_paper)
    elif current_egg == 13:
        next_paper = paper_sizes.popleft()
        paper_sizes.append(next_paper)
        paper_sizes.appendleft(current_paper)
    else:
        result = current_egg + current_paper
        if result <= 50:
            boxes_filled += 1
    if not egg_sizes or not paper_sizes:
        break

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in egg_sizes)}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")
