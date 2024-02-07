from os import truncate


def divide_numbers(num1, num2):
    print(f"{(num1 / num2):.2f}")


def add_numbers(num1, num2):
    print(f"{(num1 + num2):.2f}")


def subtract_numbers(num1, num2):
    print(f"{(num1 - num2):.2f}")


def multiply_numbers(num1, num2):
    print(f"{(num1 * num2):.2f}")


def power_numbers(num1, num2):
    result = num1 ** num2
    index = str(result).find('.')
    new_result = str(result)[0:index+3]
    print(f"{new_result}")


OPERATIONS_MAPPER = {
    "/": divide_numbers,
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
    "^": power_numbers,
}