import sys
from math import ceil

n = int(input())
max_num = -sys.maxsize
sum_num = 0

for i in range(0, n):
    num = int(input())
    if num >= max_num:
        max_num = num

    sum_num += num

if max_num == sum_num / 2:
    print("Yes")
    print(f"Sum = {ceil(sum_num / 2)}")
else:
    print("No")
    print(f"Diff = {ceil(abs(max_num - (sum_num - max_num)))}")

