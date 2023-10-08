word_list = list(filter(lambda x: len(x) % 2 == 0, input().split()))

for word in word_list:
    print(word)
