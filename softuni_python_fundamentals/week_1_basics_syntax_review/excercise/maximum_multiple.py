divisor = int(input())
boundary = int(input())

while boundary > 0:
    if boundary % divisor == 0:
        print(boundary)
        break

    boundary -= 1
