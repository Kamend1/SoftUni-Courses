sheep_queue = []

for word in input().split(", "):
    sheep_queue.append(word)

sheep_queue.reverse()

for idx in range(len(sheep_queue)):
    if idx == 0 and sheep_queue[0] == "wolf":
        print("Please go away and stop eating my sheep")
    elif sheep_queue[idx] == "wolf":
        print(f"Oi! Sheep number {idx}! You are about to be eaten by a wolf!")
