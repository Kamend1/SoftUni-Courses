from collections import deque

expression = deque(x for x in input().split())
visited = deque()
operators = ['+', '-', '*', '/']

while expression:
    character = expression.popleft()
    if character not in operators:
        visited.append(int(character))
    else:
        if character == "+":
            while len(visited) > 1:
                first_number = visited.popleft()
                second_number = visited.popleft()
                current_result = first_number + second_number
                visited.appendleft(current_result)
        elif character == "-":
            while len(visited) > 1:
                first_number = visited.popleft()
                second_number = visited.popleft()
                current_result = first_number - second_number
                visited.appendleft(current_result)
        elif character == "*":
            while len(visited) > 1:
                first_number = visited.popleft()
                second_number = visited.popleft()
                current_result = first_number * second_number
                visited.appendleft(current_result)
        elif character == "/":
            while len(visited) > 1:
                first_number = visited.popleft()
                second_number = visited.popleft()
                current_result = first_number // second_number
                visited.appendleft(current_result)
print(*visited)
