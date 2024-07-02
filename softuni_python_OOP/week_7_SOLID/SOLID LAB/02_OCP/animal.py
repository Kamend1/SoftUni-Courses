from abc import ABC, abstractmethod


class Animal(ABC):
    # def __init__(self, species):
    #     self.species = species
    @staticmethod
    @abstractmethod
    def animal_sound():
        pass


    def get_species(self):
        return self.__class__.__name__


# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')

class Cat(Animal):

    @staticmethod
    def animal_sound():
        return 'Meow'

class Dog(Animal):

    @staticmethod
    def animal_sound():
        return 'Bark'

animals = [Cat, Dog]

for animal in animals:
    print(animal.animal_sound())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
