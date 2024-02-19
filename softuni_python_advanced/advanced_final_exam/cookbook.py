def cookbook(*meals):
    cuisine_dict = {}

    for meal in meals:
        dish, cuisine, ingredient = meal
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((dish, ingredient))


    sorted_cuisine = dict(sorted(cuisine_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ""

    for k, v in sorted_cuisine.items():
        result += k + " cuisine contains " + str(len(v)) + " recipes:\n"
        for name, ingredients_list in sorted(v):
            ingredients = ', '.join(x for x in ingredients_list)
            result += "  * " + name + " -> Ingredients: " + ingredients + "\n"

    return result

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))

