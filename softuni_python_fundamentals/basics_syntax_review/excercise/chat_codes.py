n = int(input())

for i in range(n):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message > 88:
        print("Bye.")
    elif message != 86 and message < 88:
        print("GREAT!")
