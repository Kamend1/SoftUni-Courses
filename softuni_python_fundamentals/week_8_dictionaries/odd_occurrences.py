words = input().split()
dictionary = {}

for word in words:
    word_lowercase = word.lower()
    if word_lowercase not in dictionary.keys():
        dictionary[word_lowercase] = 0
    dictionary[word_lowercase] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
