period_calc = int(input())
number_doctors = 7
treated_patients = 0
untreated_patients = 0
day_count = 0

for day in range(1, period_calc + 1):
    patients_visiting = int(input())
    day_count += 1
    if treated_patients < untreated_patients and day_count % 3 == 0:
        number_doctors += 1
    if patients_visiting > number_doctors:
        untreated_patients += patients_visiting - number_doctors
        treated_patients += number_doctors
    elif patients_visiting <= number_doctors:
        treated_patients += patients_visiting

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
