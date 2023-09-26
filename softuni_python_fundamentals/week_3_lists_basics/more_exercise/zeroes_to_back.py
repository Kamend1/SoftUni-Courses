nums = [int(x) for x in input().split(", ")]

for num in nums:
    if num == 0:
        nums.remove(num)
        nums.append(num)

print(nums)
