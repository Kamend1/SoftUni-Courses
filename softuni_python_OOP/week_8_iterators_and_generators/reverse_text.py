def reverse_text(text):
    for char in text[::-1]:
        yield char

for char in reverse_text("step"):
    print(char, end='')
