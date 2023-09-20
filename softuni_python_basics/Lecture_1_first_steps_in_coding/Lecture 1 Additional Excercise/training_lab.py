w_lab_mtr = float(input())
h_lab_mtr = float(input())

number_desks_row = ((h_lab_mtr - 1) * 100) // 70
number_rows = (w_lab_mtr * 100) // 120

number_desks = number_desks_row * number_rows - 1 - 2

print(number_desks)
