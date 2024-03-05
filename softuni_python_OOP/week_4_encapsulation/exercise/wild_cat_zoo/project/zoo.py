from project.animal import Animal
from project.worker import Worker
class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price > self.__budget:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker_to_fire = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker_to_fire)
        return f"{worker_name} fired successfully"

    def pay_workers(self):

        salaries = sum([worker.salary for worker in self.workers])
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        money_to_tend = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= money_to_tend:
            self.__budget -= money_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result_string = f'You have {len(self.animals)} animals\n'
        animal_count = {}
        lion_list = []
        cheetah_list = []
        tiger_list = []
        for animal in self.animals:
            animal_type = animal.__class__.__name__
            animal_count[animal_type] = animal_count.get(animal_type, 0) + 1
            if animal_type == "Lion":
                lion_list.append(animal.__repr__())
            elif animal_type == "Cheetah":
                cheetah_list.append(animal.__repr__())
            else:
                tiger_list.append(animal.__repr__())

        result_string += f"----- {len(lion_list)} Lions:\n"
        result_string += '\n'.join(lion_list)
        result_string += f"\n----- {len(tiger_list)} Tigers:\n"
        result_string += '\n'.join(tiger_list)
        result_string += f"\n----- {len(cheetah_list)} Cheetahs:\n"
        result_string += '\n'.join(cheetah_list)

        return result_string

    def workers_status(self):
        result_string = f'You have {len(self.workers)} workers\n'
        worker_count = {}
        keeper_list = []
        caretaker_list = []
        vet_list = []
        for worker in self.workers:
            worker_type = worker.__class__.__name__
            worker_count[worker_type] = worker_count.get(worker_type, 0) + 1
            if worker_type == "Keeper":
                keeper_list.append(worker.__repr__())
            elif worker_type == "Caretaker":
                caretaker_list.append(worker.__repr__())
            else:
                vet_list.append(worker.__repr__())

        result_string += f"----- {len(keeper_list)} Keepers:\n"
        result_string += '\n'.join(keeper_list)
        result_string += f"\n----- {len(caretaker_list)} Caretakers:\n"
        result_string += '\n'.join(caretaker_list)
        result_string += f"\n----- {len(vet_list)} Vets:\n"
        result_string += '\n'.join(vet_list)

        return result_string