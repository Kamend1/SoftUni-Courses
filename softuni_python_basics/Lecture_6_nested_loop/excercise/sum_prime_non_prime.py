user_command = input()
sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0

while user_command != "stop":
    current_number = int(user_command)
    if current_number < 0:
        print("Number is negative.")
    else:
        current_number_is_prime = True
        for i in range(2, current_number):
            if current_number % i == 0:
                current_number_is_prime = False
        if current_number_is_prime:
            sum_of_prime_numbers += current_number
        else:
            sum_of_non_prime_numbers += current_number
    user_command = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
