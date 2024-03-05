from typing import List

from project.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        try:
            player_to_remove = next(filter(lambda p: p.name == player_name, self.__players))
        except StopIteration:
            return f"Player {player_name} not found"

        self.__players.remove(player_to_remove)
        return player_to_remove


