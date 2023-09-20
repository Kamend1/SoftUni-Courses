n = int(input())
is_prime = True

if n <= 1:
    is_prime = False

i = 2
while i ** 2 <= n:
    if n % i == 0:
        is_prime = False
    i += 1


if is_prime:
    print("True")
else:
    print("False")
