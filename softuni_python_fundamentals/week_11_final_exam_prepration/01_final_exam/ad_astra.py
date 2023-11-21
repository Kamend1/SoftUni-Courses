import re
from math import floor

data_string = input()
total_nutrition = 0

pattern = (r"(#(?P<food_1>[a-zA-Z\s]+)#(?P<date_1>[0-3][0-9]/[0-1][0-9]/\d{2})#(?P<nutrition_1>10000|0|[1-9][0-9]{1,"
           r"3})#|\|(?P<food_2>[a-zA-Z\s]+)\|(?P<date_2>[0-3][0-9]/[0-1][0-9]/\d{2})\|(?P<nutrition_2>10000|0|[1-9]["
           r"0-9]{1,3})\|)")

matches = re.finditer(pattern, data_string)

for match in matches:
    if '#' in match.group(1):
        total_nutrition += int(match.group('nutrition_1'))
    elif '|' in match.group(1):
        total_nutrition += int(match.group('nutrition_2'))

food_days = floor(total_nutrition / 2000)

print(f"You have food to last you for: {food_days} days!")

matches = re.finditer(pattern, data_string)

for item in matches:
    if '#' in item.group(1):
        food, exp_date, nutrition_val = item.group('food_1'), item.group('date_1'), item.group('nutrition_1')
        print(f"Item: {food}, Best before: {exp_date}, Nutrition: {nutrition_val}")
    elif '|' in item.group(1):
        food, exp_date, nutrition_val = item.group('food_2'), item.group('date_2'), item.group('nutrition_2')
        print(f"Item: {food}, Best before: {exp_date}, Nutrition: {nutrition_val}")
