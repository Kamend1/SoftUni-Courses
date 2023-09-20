volume_pool = int(input())
pipe_first_debit = int(input())
pipe_second_debit = int(input())
hours_employee_absent = float(input())

pipe_first_input = pipe_first_debit * hours_employee_absent
pipe_second_input = pipe_second_debit * hours_employee_absent
total_water_input = pipe_first_input + pipe_second_input
pipe_first_contr = (pipe_first_input / total_water_input) * 100
pipe_second_contr = (pipe_second_input / total_water_input) * 100
difference_input = abs(volume_pool - total_water_input)
percent_pool_full = (total_water_input / volume_pool) * 100

if total_water_input > volume_pool:
    print(f"For {hours_employee_absent} hours the pool overflows with {difference_input} liters.")
else:
    print(f"The pool is {percent_pool_full:.2f}% full. Pipe 1 {pipe_first_contr:.2f}%. Pipe 2 {pipe_second_contr:.2f}%.")
