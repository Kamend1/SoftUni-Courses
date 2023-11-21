import re

travel_string = input()
pattern = r"(?<=\=)[A-Z][A-Za-z]{2,}(?=\=)|(?<=\/)[A-Z][A-Za-z]{2,}(?=\/)"
valid_destinations = re.findall(pattern, travel_string)
travel_points = 0

for destination in valid_destinations:
    travel_points += len(destination)

print(f'Destinations: {", ".join(valid_destinations)}')
print(f"Travel Points: {travel_points}")
