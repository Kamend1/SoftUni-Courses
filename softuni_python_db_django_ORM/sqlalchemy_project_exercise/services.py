from main import Session
from models import Recipe, Chef


def create_recipe(name: str, ingredients: str, instructions: str):
    with Session() as session:
        recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        session.add(recipe)
        session.commit()


def update_recipe_by_name(name: str, new_name: str,  new_ingredients: str, new_instructions: str):
    with Session() as session:
        recipe = session.query(Recipe).filter_by(name=name).first()

        if recipe:
            recipe.name = new_name
            recipe.ingredients = new_ingredients
            recipe.instructions = new_instructions
            session.commit()
        else:
            print("Recipe not found")


def delete_recipe_by_name(name: str):
    with Session() as session:
        recipe = session.query(Recipe).filter_by(name=name).first()

        if recipe:
            session.delete(recipe)
            session.commit()
        else:
            print("Recipe not found")


def get_recipes_by_ingredient(ingredient_name: str):
    with Session() as session:
        search_string = f"%{ingredient_name}%"
        return session.query(Recipe).filter(Recipe.ingredients.ilike(search_string))


def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    session = Session()

    try:
        first_recipe = session.query(Recipe).filter_by(name=first_recipe_name).with_for_update.one()
        second_recipe = session.query(Recipe).filter_by(name=second_recipe_name).with_for_update.one()

        first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients

        session.commit()

    except Exception as e:
        session.rollback()
        print(f"{e}")

    finally:
        session.close()


def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
    session = Session()
    try:
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()
        chef = session.query(Chef).filter_by(name=chef_name).first()

        if recipe is None:
            raise ValueError(f"Recipe '{recipe_name}' not found.")

        if chef is None:
            raise ValueError(f"Chef '{chef_name}' not found.")

        if recipe.chef_id == chef.id:
            raise Exception(f"Recipe '{recipe_name}' is already related to Chef '{chef_name}'.")

        # recipe.chef_id = chef.id
        recipe.chef = chef
        session.commit()
        return f"Related recipe {recipe_name} with chef {chef_name}"

    except Exception as e:
        session.rollback()
        print(f"Error relating Recipe '{recipe_name}' with Chef '{chef_name}': {str(e)}")
    finally:
        session.close()


def get_recipes_with_chef():
    with Session() as session:
        # recipes = session.query(Recipe).filter(Recipe.chef_id is not None).all()
        recipes = session.query(Recipe.name, Chef.name.label('chef_name')).join(Chef, Recipe.chef).all()
        result = []

        if recipes:
            for recipy_name, chef_name in recipes:
                # chef = session.query(Chef).filter_by(id=r.chef_id).first()
                result.append(f"Recipe: {recipy_name} made by chef: {chef_name}")

            return '\n'.join(result)
        else:
            return "No recipes assigned to chefs"


# create_recipe('Spaghetti Carbonara',
#               'Pasta, Eggs, Pancetta, Cheese',
#               'Cook the pasta, mix it with eggs, pancetta, and cheese')
#
# create_recipe('Chicken Stir-Fry',
#               'Chicken, Bell Peppers, Soy Sauce, Vegetables',
#               'Stir-fry chicken and vegetables with soy sauce')
#
# create_recipe('Caesar Salad',
#               'Romaine Lettuce, Croutons, Caesar Dressing',
#               'Toss lettuce with dressing and top with croutons')
#
# with Session() as session:
#     # Query all recipes
#     recipes = session.query(Recipe).all()
#
#     # Loop through each recipe and print its details
#     for recipe in recipes:
#         print(f"Recipe name: {recipe.name}")
#
# # Update a recipe by name
# update_recipe_by_name(
#     name="Spaghetti Carbonara",
#     new_name="Carbonara Pasta",
#     new_ingredients="Pasta, Eggs, Guanciale, Cheese",
#     new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
# )
#
# with Session() as session:
#     # Query the updated recipe
#     updated_recipe = session.query(Recipe).filter_by(name="Carbonara Pasta").first()
#
#     # Print the updated recipe details
#     print("Updated Recipe Details:")
#     print(f"Name: {updated_recipe.name}")
#     print(f"Ingredients: {updated_recipe.ingredients}")
#     print(f"Instructions: {updated_recipe.instructions}")
#
# # Delete a recipe by name
# delete_recipe_by_name("Carbonara Pasta")
#
#
# with Session() as session:
#     # Query all recipes
#     recipes = session.query(Recipe).all()
#
#     # Loop through each recipe and print its details
#     for recipe in recipes:
#         print(f"Recipe name: {recipe.name}")
#
# # Delete all objects (recipes) from the database
# with Session() as session:
#     session.query(Recipe).delete()
#     session.commit()
#
# # Create three Recipe instances with two of them sharing the same ingredient
# recipe1 = create_recipe(
#     'Spaghetti Bolognese',
#     'Ground beef, tomatoes, pasta',
#     'Cook beef, add tomatoes, serve over pasta'
# )
#
# recipe2 = create_recipe(
#     'Chicken Alfredo',
#     'Chicken, fettuccine, Alfredo sauce',
#     'Cook chicken, boil pasta, mix with sauce'
# )
#
# recipe3 = create_recipe(
#     'Chicken Noodle Soup',
#     'Chicken, noodles, carrots',
#     'Boil chicken, add noodles, carrots'
# )
#
# # Run the function and print the results
# ingredient_to_filter = 'Chicken'
# filtered_recipes = get_recipes_by_ingredient('Chicken')
#
# print(f"Recipes containing {ingredient_to_filter}:")
# for recipe in filtered_recipes:
#     print(f"Recipe name - {recipe.name}")
#
# # Create the first recipe
# create_recipe("Pancakes", "Flour, Eggs, Milk", "Mix and cook on a griddle")
#
# # Create the second recipe
# create_recipe("Waffles", "Flour, Eggs, Milk, Baking Powder", "Mix and cook in a waffle iron")
#
# # Now, swap their ingredients
# swap_recipe_ingredients_by_name("Pancakes", "Waffles")
#
# recipe1 = session.query(Recipe).filter_by(name="Pancakes").first()
# recipe2 = session.query(Recipe).filter_by(name="Waffles").first()
# print(f"Pancakes ingredients {recipe1.ingredients}")
# print(f"Waffles ingredients {recipe2.ingredients}")
#

# # Create a recipe instance for Bulgarian Musaka
# musaka_recipe = Recipe(
#     name="Musaka",
#     ingredients="Potatoes, Ground Meat, Onions, Eggs, Milk, Cheese, Spices",
#     instructions="Layer potatoes and meat mixture, pour egg and milk mixture on top, bake until golden brown."
# )
#
# # Create a Bulgarian chef instances
# bulgarian_chef1 = Chef(name="Ivan Zvezdev")
# bulgarian_chef2 = Chef(name="Uti Buchvarov")
#
# with Session() as session:
#     # Add the recipe instance to the session
#     session.add(musaka_recipe)
#
#     # Add the chef instances to the session
#     session.add(bulgarian_chef1)
#     session.add(bulgarian_chef2)
#
#     # Commit the changes to the database
#     session.commit()

# print(relate_recipe_with_chef_by_name("Musaka", "Ivan Zvezdev"))

# # Create chef instances
# chef1 = Chef(name="Gordon Ramsay")
# chef2 = Chef(name="Julia Child")
# chef3 = Chef(name="Jamie Oliver")
# chef4 = Chef(name="Nigella Lawson")
#
# # Create recipe instances associated with chefs
# recipe1 = Recipe(name="Beef Wellington", ingredients="Beef fillet, Puff pastry, Mushrooms, Foie gras", instructions="Prepare the fillet and encase it in puff pastry.")
#
# recipe2 = Recipe(name="Boeuf Bourguignon", ingredients="Beef, Red wine, Onions, Carrots", instructions="Slow-cook the beef with red wine and vegetables.")
#
# recipe3 = Recipe(name="Spaghetti Carbonara", ingredients="Spaghetti, Eggs, Pancetta, Cheese", instructions="Cook pasta, mix ingredients.")
#
# recipe4 = Recipe(name="Chocolate Cake", ingredients="Chocolate, Flour, Sugar, Eggs", instructions="Bake a delicious chocolate cake.")
#
# recipe5 = Recipe(name="Chicken Tikka Masala", ingredients="Chicken, Yogurt, Tomatoes, Spices", instructions="Marinate chicken and cook in a creamy tomato sauce.")
#
# recipe1.chef = chef1
# recipe2.chef = chef2
# recipe3.chef = chef3
# recipe4.chef = chef4
# recipe5.chef = chef3
#
# with Session() as session:
#     session.add_all([chef1, chef2, chef3, chef4, recipe1, recipe2, recipe3, recipe4, recipe5])
#     session.commit()
#
#
# print(get_recipes_with_chef())
