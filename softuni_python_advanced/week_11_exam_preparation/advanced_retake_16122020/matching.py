from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    elif males[-1] % 25 == 0:
        for _ in range(2):
            if males:
                males.pop()
            else:
                break
        continue
    else:
        current_male = males[-1]

    if females[0] <= 0:
        females.popleft()
        continue
    elif females[0] % 25 == 0:
        for _ in range(2):
            if females:
                females.popleft()
            else:
                break
        continue
    else:
        current_female = females[0]

    if current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
