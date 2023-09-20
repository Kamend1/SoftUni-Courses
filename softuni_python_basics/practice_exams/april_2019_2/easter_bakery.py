price_flour_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
number_egg_cartons = int(input())
number_yeast_pkt = int(input())
price_sugar_kg = price_flour_kg * 0.75
price_egg_carton = price_flour_kg * 1.10
price_yeast_pkt = price_sugar_kg * 0.20

amount_needed = price_flour_kg * kg_flour \
                + price_sugar_kg * kg_sugar \
                + price_egg_carton * number_egg_cartons \
                + price_yeast_pkt * number_yeast_pkt

print(f"{amount_needed:.2f}")
