parenthesis_string = input()
parenthesis_stack = []
unbalanced_closing = False

for current_char in parenthesis_string:
    if current_char == '{':
        parenthesis_stack.append(current_char)
    elif current_char == '(':
        parenthesis_stack.append(current_char)
    elif current_char == '[':
        parenthesis_stack.append(current_char)
    elif current_char == '}':
        if parenthesis_stack:
            last_open_char = parenthesis_stack.pop()
            if last_open_char != "{":
                parenthesis_stack.append(last_open_char)
        else:
            unbalanced_closing = True
    elif current_char == ')':
        if parenthesis_stack:
            last_open_char = parenthesis_stack.pop()
            if last_open_char != "(":
                parenthesis_stack.append(last_open_char)
        else:
            unbalanced_closing = True
    elif current_char == ']':
        if parenthesis_stack:
            last_open_char = parenthesis_stack.pop()
            if last_open_char != "[":
                parenthesis_stack.append(last_open_char)
        else:
            unbalanced_closing = True

if parenthesis_stack or unbalanced_closing:
    print("NO")
else:
    print("YES")
