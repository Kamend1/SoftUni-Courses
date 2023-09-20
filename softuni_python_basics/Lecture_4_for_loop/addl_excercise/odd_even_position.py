from math import inf

n = int(input())
OddMin = float(inf)
OddMax = -float(inf)
OddSum = 0
EvenMin = float(inf)
EvenMax = -float(inf)
EvenSum = 0

for i in range(1, n + 1):
    num = float(input())
    if i % 2 != 0:
        if num < OddMin:
            OddMin = num
        if num > OddMax:
            OddMax = num
        OddSum += num
    elif i % 2 == 0:
        if num < EvenMin:
            EvenMin = num
        if num > EvenMax:
            EvenMax = num
        EvenSum += num

print(f"OddSum={OddSum:.2f},")
if OddMin == float(inf):
    print("OddMin=No,")
else:
    print(f"OddMin={OddMin:.2f},")
if OddMax == -float(inf):
    print("OddMax=No,")
else:
    print(f"OddMax={OddMax:.2f},")

print(f"EvenSum={EvenSum:.2f},")
if EvenMin == float(inf):
    print("EvenMin=No,")
else:
    print(f"EvenMin={EvenMin:.2f},")
if EvenMax == -float(inf):
    print("EvenMax=No")
else:
    print(f"EvenMax={EvenMax:.2f}")
