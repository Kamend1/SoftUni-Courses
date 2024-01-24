def palindrome(word, idx=0):
    is_palindrome = True
    n = len(word) // 2
    while idx < n:
        if word[idx] != word[(-idx - 1)]:
            is_palindrome = False
            break

        idx += 1
        palindrome(word, idx)

    if is_palindrome:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))