n = int(input())
sum_left = 0
sum_right = 0

for i in range(0, n):
    left_num = int(input())
    sum_left += left_num

for i in range(0, n):
    right_num = int(input())
    sum_right += right_num

difference = abs(sum_left - sum_right)

if difference == 0:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {difference}")
