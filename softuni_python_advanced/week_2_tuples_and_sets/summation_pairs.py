numbers = [int(x) for x in input().split()]
target = int(input())

targets = set()
value_map = {}

for value in numbers:
    resulting_number = target - value
    targets.add(resulting_number)
    value_map[resulting_number] = value

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = value_map[value]
        del value_map[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        value_map[resulting_number] = value
