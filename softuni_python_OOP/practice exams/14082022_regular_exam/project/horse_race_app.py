from typing import List

from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_specification.appaloosa import Appaloosa
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses: List[Appaloosa: Horse, Thoroughbred: Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []
        self.created_race_types: List[str] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = next(filter(lambda h: h.name == horse_name, self.horses), None)

        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            horse_object = globals()[horse_type]
            new_horse = horse_object(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)

        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in self.created_race_types:
            raise Exception(f"Race {race_type} has been already created!")

        self.created_race_types.append(race_type)
        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse_to_add = None
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type:
                if not horse.is_taken:
                    horse_to_add = horse
                    break
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if horse_to_add:
            if not jockey.horse:
                jockey.horse = horse_to_add
                horse_to_add.is_taken = True
                return f"Jockey {jockey_name} will ride the horse {horse_to_add.name}."
            else:
                return f"Jockey {jockey_name} already has a horse."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        max_speed = 0
        winner = None
        for jockey in race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner = jockey

        return (f"The winner of the {race_type} race, "
                f"with a speed of {max_speed}km/h is {winner.name}! "
                f"Winner's horse: {winner.horse.name}.")
