expression = input()

open_parenthesis_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        open_parenthesis_stack.append(index)
    elif expression[index] == ")":
        start_index = open_parenthesis_stack.pop()
        end_index = index + 1
        print(expression[start_index:end_index])
