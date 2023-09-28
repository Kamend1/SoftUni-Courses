beggar_offers = [int(x) for x in input().split(',')]
number_beggars = int(input())

output_beggar_takings = []

for current_beggar in range(number_beggars):
    sum_current = sum(beggar_offers[current_beggar ::number_beggars])
    output_beggar_takings.append(sum_current)

print(output_beggar_takings)
