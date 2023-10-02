def aliquot_sum(number):
    aliquot_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            aliquot_sum += divisor
    return aliquot_sum

number = int(input())

if number == aliquot_sum(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
