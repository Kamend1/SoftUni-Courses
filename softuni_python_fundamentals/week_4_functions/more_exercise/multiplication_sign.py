def multiplication_sign(num1, num2, num3):
    counter_negative = 0
    is_zero = False
    if num1 < 0:
        counter_negative += 1
    elif num1 == 0:
        is_zero = True
    if num2 < 0:
        counter_negative += 1
    elif num2 == 0:
        is_zero = True
    if num3 < 0:
        counter_negative += 1
    elif num3 == 0:
        is_zero = True
    if (counter_negative == 0 or counter_negative == 2) and not is_zero:
        return "positive"
    elif (counter_negative == 1 or counter_negative == 3) and not is_zero:
        return "negative"
    elif is_zero:
        return "zero"

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(multiplication_sign(num1, num2, num3))
