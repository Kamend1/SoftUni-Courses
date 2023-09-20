number_input = int(input())

if number_input < 100:
    print("Less than 100")
elif 100 <= number_input <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
