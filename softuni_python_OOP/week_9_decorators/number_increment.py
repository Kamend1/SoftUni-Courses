def number_increment(numbers):

    def increase():
        new_list = [el + 1 for el in numbers]
        return new_list

    return increase()

print(number_increment([1, 2, 3]))
