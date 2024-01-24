from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
matches_count = 0
worms_without_holes = len(worms)

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    if current_worm == current_hole:
        matches_count += 1
        worms_without_holes -= 1
    else:
        if current_worm - 3 > 0:
            worms.append(current_worm - 3)

print(f"Matches: {matches_count}" if matches_count > 0 else "There are no matches.")
if not worms:
    if worms_without_holes == 0:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(worm) for worm in worms)}")
print(f"Holes left: {', '.join(str(hole) for hole in holes)}" if holes else "Holes left: none")
