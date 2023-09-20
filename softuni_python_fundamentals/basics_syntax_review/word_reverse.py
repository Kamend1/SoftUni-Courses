word = input()

reversed_word = []

for i in range(len(word) -1, -1, -1):
    reversed_word.append(word[i])

print("".join(reversed_word))
