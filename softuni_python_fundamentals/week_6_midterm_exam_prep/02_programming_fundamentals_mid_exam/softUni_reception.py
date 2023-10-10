from math import ceil

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_students = int(input())

total_students_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours_counter_list = []
hours_counter = 0


while number_students > 0:
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter_list.append(0)
        continue
    else:
        if total_students_per_hour < number_students:
            hours_counter_list.append(total_students_per_hour)
            number_students -= total_students_per_hour
        elif total_students_per_hour >= number_students:
            hours_counter_list.append(number_students)
            number_students = 0

print(f"Time needed: {len(hours_counter_list)}h.")
