n = int(input())
open_bracket = 0
is_balanced = False

for i in range(n):
    user_input = input()
    if user_input == "(" and open_bracket == 0:
        open_bracket = 1
        is_balanced = False
    elif user_input == "(" and open_bracket == 1:
        is_balanced = False
        break
    if user_input == ")" and open_bracket == 1:
        open_bracket = 0
        is_balanced = True
    elif user_input == ")" and open_bracket == 0:
        is_balanced = False
        break

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
