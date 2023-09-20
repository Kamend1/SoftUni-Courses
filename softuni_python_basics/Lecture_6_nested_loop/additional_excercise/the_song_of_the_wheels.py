number_m = int(input())
is_password_valid = False
counter_valid_passwords = 0
valid_password = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                current_password = str(a) + str(b) + str(c) + str(d)
                if a < b and c > d and a * b + c * d == number_m:
                    print(current_password, end=" ")
                    counter_valid_passwords += 1
                    if counter_valid_passwords == 4:
                        valid_password = current_password

if counter_valid_passwords >= 4:
    print(f"\nPassword: {valid_password}")
else:
    print("\nNo!")
