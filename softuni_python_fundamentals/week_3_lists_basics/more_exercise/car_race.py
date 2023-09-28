times = [int(x) for x in input().split(" ")]
winner = ""
time_left = 0
time_right = 0
best_time = 0
left_idx = 0
right_idx = -1

for _ in range(len(times) // 2):
    time_left += times[left_idx]
    time_right += times[right_idx]
    if times[left_idx] == 0:
        time_left *= 0.8
    if times[right_idx] == 0:
        time_right *= 0.8
    left_idx += 1
    right_idx -= 1

if time_left < time_right:
    winner = "left"
    best_time = time_left
else:
    winner = "right"
    best_time = time_right

print(f"The winner is {winner} with total time: {best_time:.1f}")
