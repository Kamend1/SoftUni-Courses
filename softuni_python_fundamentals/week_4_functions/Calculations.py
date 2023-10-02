def calculate(num_1, num_2, operation):
    if operation == 'add':
        result = num_1 + num_2
    elif operation == 'subtract':
        result = num_1 - num_2
    elif operation == 'multiply':
        result = num_1 * num_2
    elif operation == 'divide':
        result = int(num_1 / num_2)
    return result

operation = input()
num_1 = int(input())
num_2 = int(input())

print(calculate(num_1, num_2, operation))
