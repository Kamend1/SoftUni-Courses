targets = [int(x) for x in input().split()]
shot_targets = ["No"] * len(targets)
shots_targets_counter = 0

user_command = input()

while user_command != "End":
    index = int(user_command)
    if index < 0 or index >= len(targets):
        pass
    else:
        for idx in range(len(targets)):
            if shot_targets[index] == "No":
                if idx == index:
                    continue
                if targets[idx] > targets[index] and shot_targets[idx] == "No":
                    targets[idx] -= targets[index]
                elif targets[idx] <= targets[index] and shot_targets[idx] == "No":
                    targets[idx] += targets[index]
        targets[index] = - 1
        shot_targets[index] = "Yes"
        shots_targets_counter += 1

    user_command = input()

print(f'Shot targets: {shots_targets_counter} -> {" ".join(map(str, targets))}')
