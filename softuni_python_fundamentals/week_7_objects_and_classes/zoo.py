class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == ("bird"):
            result = f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result

name_of_zoo = input()
number_animals = int(input())

zoo = Zoo(name_of_zoo)

for i in range(number_animals):
    animal_input = input().split()
    zoo.add_animal(animal_input[0], animal_input[1])

searched_species = input()
result = zoo.get_info(searched_species)
print(result)
