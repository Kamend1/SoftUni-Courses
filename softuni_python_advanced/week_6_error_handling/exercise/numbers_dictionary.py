numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line

    try:
        number = int(input())

    except ValueError:
        print("The variable number must be an integer")
        break

    numbers_dictionary[number_as_string] = number

    line = input()

line = input()

while line != "Remove":
    searched = line

    try:
        print(numbers_dictionary[searched])

    except KeyError:
        print:("Number does not exist in dictionary")
        break

    line = input()

line = input()

while line != "End":
    searched = line

    try:
        del numbers_dictionary[searched]

    except KeyError:
        print("Number does not exist in dictionary")
        break

    line = input()

print(numbers_dictionary)
