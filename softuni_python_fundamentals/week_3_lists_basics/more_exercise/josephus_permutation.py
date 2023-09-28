numbers = list(int(x) for x in input().split(" "))
k = int(input())
josephus_permutation = []
idx = 0
position = 1

while numbers:
    if idx > len(numbers) - 1:
        idx = 0
    if position % k == 0:
        josephus_permutation.append(numbers.pop(idx))

        position += 1
        continue
    position += 1
    idx += 1
print(f"[{','.join(list(map(str, josephus_permutation)))}]")
