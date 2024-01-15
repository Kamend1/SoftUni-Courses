expression = input()

symbol_counter = {}

for symbol in expression:
    if symbol not in symbol_counter:
        symbol_counter[symbol] = 0
    symbol_counter[symbol] += 1

for symbol, count in sorted(symbol_counter.items()):
    print(f"{symbol}: {count} time/s")
