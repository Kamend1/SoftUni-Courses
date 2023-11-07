string = input()
unique_string = ""
current_string = ""
current_digit_string = ""
string_to_print = ""
previous_char = "alpha"

for char in string:
    if not char.isdigit():
        if char.isalpha():
            if char.lower() not in unique_string:
                unique_string += char.lower()
        else:
            if char not in unique_string:
                unique_string += char
        if previous_char == 'digit':
            digit = int(current_digit_string)
            string_to_print += current_string * digit
            current_string = ""
            current_digit_string = ""
            if char.isalpha():
                current_string += char.upper()
            else:
                current_string += char
            previous_char = 'alpha'
        else:
            if char.isalpha():
                current_string += char.upper()
                previous_char = 'alpha'
            else:
                current_string += char
                previous_char = 'alpha'
    elif char.isdigit():
        if previous_char == 'digit':
            current_digit_string += char
            digit = int(current_digit_string)
            string_to_print += current_string * digit
            current_string = ""
            current_digit_string = ""
            previous_char = 'alpha'
        else:
            current_digit_string += char
            previous_char = 'digit'

if previous_char == 'digit':
    digit = int(current_digit_string)
    string_to_print += current_string * digit
    current_string = ""
    current_digit_string = ""
    previous_char = 'alpha'

print(f"Unique symbols used: {len(unique_string)}")
print(string_to_print)
