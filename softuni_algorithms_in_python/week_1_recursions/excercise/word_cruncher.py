def find_all_solutions(idx, target_word, words_by_idx, word_count, used_words):
    if idx >= len(target_word):
        print(' '.join(used_words))
        return
    if idx not in words_by_idx:
        return
    for word in words_by_idx[idx]:
        if word_count[word] == 0:
            continue
        used_words.append(word)
        word_count[word] -= 1

        find_all_solutions(idx + len(word), target_word, words_by_idx, word_count, used_words)

        used_words.pop()
        word_count[word] += 1


user_words = input().split(", ")
target_word = input()

words_by_idx = {}
word_count = {}

for word in user_words:
    if word in word_count:
        word_count[word] += 1
        continue

    word_count[word] = 1

    try:
        idx = 0
        while True:
            idx = target_word.index(word, idx)

            if idx not in words_by_idx:
                words_by_idx[idx] = []
            words_by_idx[idx].append(word)
            idx += len(word)
    except ValueError:
        pass

find_all_solutions(0, target_word, words_by_idx, word_count, [])
