from collections import deque

words = {
    "rose": ["", "", "", ""],
    "tulip": ["", "", "", "", ""],
    "lotus": ["", "", "", "", ""],
    "daffodil": ["", "", "", "", "", "", "", ""]
}

vowels = deque(input().split())
consonants = input().split()
word_found = False


while True:
    if not vowels or not consonants:
        break

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in words:
        if current_vowel in word:
            count_vowel = word.count(current_vowel)
            idx = 0
            while count_vowel > 0:
                if current_vowel == word[idx]:
                    words[word][idx] = current_vowel
                    count_vowel -= 1
                idx += 1

        if current_consonant in word:
            count_consonant = word.count(current_consonant)
            idx = 0
            while count_consonant > 0:
                if current_consonant == word[idx]:
                    words[word][idx] = current_consonant
                    count_consonant -= 1
                idx += 1

        if not "" in words[word]:
            print(f'Word found: {word}')
            word_found = True

    if word_found:
        break

if not word_found:
    print('Cannot find any word!')
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
