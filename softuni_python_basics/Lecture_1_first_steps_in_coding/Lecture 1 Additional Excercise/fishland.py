price_skumria_kg = float(input())
price_caca_kg = float(input())
qty_palamud = float(input())
qty_safrid = float(input())
qty_midi = int(input())

price_palamud_kg = 1.6 * price_skumria_kg
price_safrid_kg = 1.8 * price_caca_kg
price_midi_kg = 7.50

amount = qty_midi * price_midi_kg \
         + qty_palamud * price_palamud_kg \
         + qty_safrid * price_safrid_kg

print(f"{amount:.2f}")
