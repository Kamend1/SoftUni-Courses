beginning_val_first_couple = int(input())
beginning_val_second_couple = int(input())
difference_first_couple = int(input())
difference_second_couple = int(input())
ending_val_first_couple = beginning_val_first_couple + difference_first_couple
ending_val_second_couple = beginning_val_second_couple + difference_second_couple
first_couple_is_prime = False
second_couple_is_prime = False

for first_couple in range(beginning_val_first_couple, ending_val_first_couple + 1):
    first_couple_is_prime = True
    for i in range(2, first_couple):
        if first_couple % i == 0:
            first_couple_is_prime = False
            break
    if first_couple_is_prime:
        first_couple_str = str(first_couple)
        for second_couple in range(beginning_val_second_couple, ending_val_second_couple + 1):
            second_couple_is_prime = True
            for j in range(2, second_couple):
                if second_couple % j == 0:
                    second_couple_is_prime = False
                    break
            if second_couple_is_prime:
                second_couple_str = str(second_couple)
            if first_couple_is_prime and second_couple_is_prime:
                prime_pair_number = first_couple_str + second_couple_str
                print(prime_pair_number)
