# my solution before exercise
# from collections import deque
#
# expression = deque(x for x in input().split())
# visited = deque()
#
# while expression:
#     character = expression.popleft()
#     if character not in "+-*/":
#         visited.append(int(character))
#     else:
#         if character == "+":
#             while len(visited) > 1:
#                 visited.appendleft(visited.popleft() + visited.popleft())
#         elif character == "-":
#             while len(visited) > 1:
#                 visited.appendleft(visited.popleft() - visited.popleft())
#         elif character == "*":
#             while len(visited) > 1:
#                 visited.appendleft(visited.popleft() * visited.popleft())
#         elif character == "/":
#             while len(visited) > 1:
#                 visited.appendleft(visited.popleft() // visited.popleft())
#
# print(*visited)

#lecturer fancy solution, new function reduce
from functools import reduce
expression = input().split()

functions = {
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a // b, map(int, expression[:i])),
}

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element in "+-*/":
        expression[0] = functions[element](idx)
        [expression.pop(1) for _ in range(idx)] # pop everything including the operator
        idx = 1

    idx += 1

print(expression[0])
