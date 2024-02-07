import softuni_python_advanced.week_9_modules.mathematical_operations.operations_mapper as op

first_number, sign, second_number = input().split()

function_name = op.OPERATIONS_MAPPER.get(sign)

function_name(float(first_number), float(second_number))
