import re

number_inputs = int(input())

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"

inputs = []
for _ in range(number_inputs):
    user_input = input()
    inputs.append(user_input)

for item in inputs:
    match = re.findall(pattern, item)
    if match:
        print(f"{match[0][0]}, The {match[0][1]}\n>> Strength: {len(match[0][0])}\n>> Armor: {len(match[0][1])}")
    else:
        print("Access denied!")
