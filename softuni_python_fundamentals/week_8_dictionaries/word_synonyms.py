number_of_words = int(input())
words = {}

for i in range(number_of_words):
    word = input()
    synonym = input()
    if word not in words.keys():
        words[word] = []
        words[word].append(synonym)
    else:
        words[word].append(synonym)

for key in words.keys():
    values_str = ', '.join(words[key])
    print(f"{key} - {values_str}")
