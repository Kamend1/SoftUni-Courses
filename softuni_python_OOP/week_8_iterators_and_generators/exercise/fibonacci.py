def fibonacci():

    # num_1 = 0
    # num_2 = 1
    # yield num_1
    # yield num_2
    #
    # while True:
    #     current = num_1 + num_2
    #     yield current
    #     num_1 = num_2
    #     num_2 = current

    num_1, num_2 = 0, 1

    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


generator = fibonacci()
for i in range(5):
    print(next(generator))

