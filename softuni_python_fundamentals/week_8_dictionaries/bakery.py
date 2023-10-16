data_input = input().split()
bakery = {}

for i in range(0, len(data_input), 2):
    key, value = data_input[i], data_input[i + 1]
    bakery[key] = int(value)

print(bakery)
