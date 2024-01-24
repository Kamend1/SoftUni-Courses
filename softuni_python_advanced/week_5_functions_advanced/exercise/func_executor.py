def func_executor(*args):
    string = ''
    print(args)
    for element in args:
        function_name, current_args = element
        result = function_name(*current_args)
        string += f"{function_name} - {result}\n"
    return string

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
