string = input()
digits = ""
letters = ""
other = ""

for chr in string:
    if chr.isalpha():
        letters += chr
    elif chr.isdigit():
        digits += chr
    else:
        other += chr

print(f"{digits}\n{letters}\n{other}")
