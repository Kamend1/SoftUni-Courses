n = int(input())
sum_even = 0
sum_odd = 0

for i in range(0, n):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    elif i % 2 != 0:
        sum_odd += num

difference = abs(sum_even - sum_odd)

if difference == 0:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    print("No")
    print(f"Diff = {difference}")
