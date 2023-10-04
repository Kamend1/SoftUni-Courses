employee_happiness = [int(x) for x in input().split()]
corrective_factor = int(input())

factored_exmployee_happiness = []
happy_counter = 0

for idx in range(len(employee_happiness)):
    factored_exmployee_happiness.append(employee_happiness[idx] * corrective_factor)

average_happiness = sum(factored_exmployee_happiness) / len(factored_exmployee_happiness)

for idx in range(len(factored_exmployee_happiness)):
    if factored_exmployee_happiness[idx] > average_happiness:
        happy_counter += 1

if happy_counter >= len(factored_exmployee_happiness) // 2:
    print(f"Score: {happy_counter}/{len(factored_exmployee_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_counter}/{len(factored_exmployee_happiness)}. Employees are not happy!")
