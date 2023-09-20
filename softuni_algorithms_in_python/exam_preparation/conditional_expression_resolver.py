def evaluate_expression(expression, idx):
    if expression[idx].isdigit():
        return expression[idx]
    if expression[idx] == 't':
        return evaluate_expression(expression, idx + 2)

    cursor = idx + 2
    conditional_counter = 0
    while True:
        symbol = expression[cursor]
        if symbol == '?':
            conditional_counter += 1
        elif symbol == ':':
            if conditional_counter == 0:
                return evaluate_expression(expression, cursor + 1)
            conditional_counter -= 1
        cursor += 1



input_str = input()
expression = input_str.replace(" ", "")
result = evaluate_expression(expression, 0)

print(result)
