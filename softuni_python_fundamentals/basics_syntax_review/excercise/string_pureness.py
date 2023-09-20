n = int(input())
is_pure = True

for i in range(n):
    string = input()

    if "," in string or "." in string or "_" in string:
        is_pure = False
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
