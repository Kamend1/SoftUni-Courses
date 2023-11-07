string = input()
cipher_string = ""

for char in string:
    cipher_string += chr(ord(char) + 3)

print(cipher_string)
