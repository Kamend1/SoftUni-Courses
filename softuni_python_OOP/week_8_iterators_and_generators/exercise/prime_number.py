from math import sqrt


def get_primes(my_list):

    for number in my_list:
        flag = False
        if number > 0 and number != 1:
            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    flag = True
                    break

            if not flag:
                yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))