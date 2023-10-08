pokemons = [int(x) for x in input().split()]
removed_pokemons = []

while pokemons:
    index = int(input())
    if index < 0:
        popped_item = pokemons.pop(0)
        removed_pokemons.append(popped_item)
        pokemons.insert(0, pokemons[-1])
    elif index >= len(pokemons):
        popped_item = pokemons.pop(-1)
        removed_pokemons.append(popped_item)
        pokemons.append(pokemons[0])
    else:
        popped_item = pokemons.pop(index)
        removed_pokemons.append(popped_item)
    for idx in range(len(pokemons)):
        if pokemons[idx] > popped_item:
            pokemons[idx] -= popped_item
        elif pokemons[idx] <= popped_item:
            pokemons[idx] += popped_item

print(sum(removed_pokemons))
