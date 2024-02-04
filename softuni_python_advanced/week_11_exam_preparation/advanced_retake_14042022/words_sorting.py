def words_sorting(*words):
    words_dict = {}
    values = 0
    result = ""
    for word in words:
        words_dict[word] = 0
        current_value = 0
        for letter in word:
            current_value += ord(letter)
        words_dict[word] += current_value
        values += current_value

    if values % 2 == 0:
        sorted_words = dict(sorted(words_dict.items(), key=lambda x: x[0]))
        for k, v in sorted_words.items():
            result += f"{k} - {v}\n"
    else:
        sorted_words = dict(sorted(words_dict.items(), key=lambda x: -x[1]))
        for k, v in sorted_words.items():
            result += f"{k} - {v}\n"

    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
