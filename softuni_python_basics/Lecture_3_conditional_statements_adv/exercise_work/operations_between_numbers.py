first_number = int(input())
second_number = int(input())
operator = str(input())
calc_result = 0
even_or_odd = ""

if operator == "+" or operator == "*" or operator == "-":
    if operator == "+":
        calc_result = first_number + second_number
        if calc_result % 2 == 0:
            even_or_odd = "even"
        else:
            even_or_odd = "odd"
    elif operator == "-":
        calc_result = first_number - second_number
        if calc_result % 2 == 0:
            even_or_odd = "even"
        else:
            even_or_odd = "odd"
    elif operator == "*":
        calc_result = first_number * second_number
        if calc_result % 2 == 0:
            even_or_odd = "even"
        else:
            even_or_odd = "odd"
    print(f"{first_number} {operator} {second_number} = {calc_result} - {even_or_odd}")
elif operator == "/" or operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        if operator == "/":
            calc_result = first_number / second_number
            print(f"{first_number} / {second_number} = {calc_result:.2f}")
        elif operator == "%":
            calc_result = first_number % second_number
            print(f"{first_number} % {second_number} = {calc_result}")
