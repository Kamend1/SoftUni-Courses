def loading_bar(number):
    if 0 <= number <= 99:
        result = "[" + "%" * (number // 10) + "." * ((100 - number) // 10) + "]"
        print(f"{number}% {result}\nStill loading...")
    elif number == 100:
        result = "[%%%%%%%%%%]"
        print(f"100% Complete!\n{result}")

status = int(input())

loading_bar(status)
