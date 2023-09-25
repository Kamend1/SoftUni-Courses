num_characters = int(input())
sum_characters = 0

for i in range(num_characters):
    input_char = input()
    sum_characters += ord(input_char)

print(f"The sum equals: {sum_characters}")
