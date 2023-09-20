number = int(input())

print("+" + " -" * (number - 2) + " +")
for i in range(1, number - 1):
    print(chr(124) + " -" * (number - 2) + " " + chr(124))
print("+" + " -" * (number - 2) + " +")
