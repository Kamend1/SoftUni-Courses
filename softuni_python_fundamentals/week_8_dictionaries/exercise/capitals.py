countries = [str(x) for x in input().split(", ")]
capitals = [str(x) for x in input().split(", ")]
country_capital_dict = {}

for country, capital in zip(countries, capitals):
    country_capital_dict[country] = capital

for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
