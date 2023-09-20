budget = int(input())

shopping_input = input()

while shopping_input != "End":
    budget -= int(shopping_input)
    if budget < 0:
        print("You went in overdraft!")
        break
    else:
        shopping_input = input()

if shopping_input == "End":
    print("You bought everything needed.")
