factor = int(input())
count = int(input())
multiples_list = []

for num in range(1, count + 1):
    multple = factor * num
    multiples_list.append(multple)

print(multiples_list)
