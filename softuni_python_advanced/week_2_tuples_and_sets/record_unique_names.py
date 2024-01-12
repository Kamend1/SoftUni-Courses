counter = int(input())
names = []
for _ in range(counter):
    names.append(input())

# unique_names = set(names)
unique_names = {name for name in names}

for name in unique_names:
    print(name)
