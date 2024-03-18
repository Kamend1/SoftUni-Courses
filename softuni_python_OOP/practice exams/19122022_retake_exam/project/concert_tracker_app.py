from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = ['Guitarist', "Drummer", "Singer"]

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Guitarist: Musician, Drummer: Musician, Singer: Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        musician = next(filter(lambda m: m.name == name, self.musicians), None)
        if musician:
            raise Exception(f"{name} is already a musician!")

        musician_object = globals()[musician_type]
        new_musician = musician_object(name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next(filter(lambda b: b.name == name, self.bands), None)

        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = next(filter(lambda c: c.place == place, self.concerts), None)

        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next(filter(lambda m: m.name == musician_name, self.musicians), None)
        band = next(filter(lambda b: b.name == band_name, self.bands), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands), None)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = next(filter(lambda m: m.name == musician_name, band.members), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        if not band.can_play():
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not band.members_have_needed_skills(concert.genre):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
