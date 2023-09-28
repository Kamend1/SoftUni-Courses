nums = [int(x) for x in input().split(" ")]
string = input()
message = ""


for idx in range(len(nums)):
    num = str(nums[idx])
    sum_idx = 0
    for digit in num:
        sum_idx += int(digit)
    if sum_idx >= len(string):
        new_idx = sum_idx - len(string) * (sum_idx // len(string))
    else:
        new_idx = sum_idx
    message += string[new_idx]
    string = string[:new_idx] + string[new_idx + 1:]

print(message)
