string_deck = list(input().split(" "))
shuffle_count = int(input())
shuffled_deck = []

string_deck_first = string_deck[0:(len(string_deck) // 2)]
string_deck_second = string_deck[(len(string_deck) // 2):]


for i in range(shuffle_count):
    shuffled_deck = []
    for j in range(len(string_deck_first)):
        shuffled_deck.append(string_deck_first[j])
        shuffled_deck.append(string_deck_second[j])
    string_deck = shuffled_deck
    string_deck_first = string_deck[0:(len(string_deck) // 2)]
    string_deck_second = string_deck[(len(string_deck) // 2):]


print(shuffled_deck)
