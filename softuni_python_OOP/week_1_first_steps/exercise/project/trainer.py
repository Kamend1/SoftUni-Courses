from softuni_python_OOP.week_1_first_steps.exercise.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon_list = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon_list:
            self.pokemon_list.append(pokemon)
            details = pokemon.pokemon_details().split()
            return f"Caught {details[0]} with health {details[-1]}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemon_list:
            if pokemon.name == pokemon_name:
                self.pokemon_list.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemon_list)}\n"

        for pokemon in self.pokemon_list:
            result += f"- {pokemon.pokemon_details()}\n"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

