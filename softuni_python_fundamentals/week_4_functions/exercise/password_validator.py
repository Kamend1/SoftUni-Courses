def password_validator(password):
    length_correct = True
    number_digits = 0
    enough_digits = True
    only_letters_digits = True
    if len(password) < 6 or len(password) > 10:
        length_correct = False
    for char in password:
        if char.isdigit():
            number_digits += 1
        if not char.isdigit():
            if ord(char) < 65 or 91 <= ord(char) <= 96 or ord(char) > 122:
                only_letters_digits = False
    if number_digits < 2:
        enough_digits = False
    if length_correct and enough_digits and only_letters_digits:
        print("Password is valid")
    if not length_correct:
        print("Password must be between 6 and 10 characters")
    if not only_letters_digits:
        print("Password must consist only of letters and digits")
    if not enough_digits:
        print("Password must have at least 2 digits")

password = input()
password_validator(password)
