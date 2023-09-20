while True:
    num = float(input())
    if num < 0:
        print("Negative number!")
        break
    else:
        result = num * 2
        print(f"Result: {result:.2f}")
