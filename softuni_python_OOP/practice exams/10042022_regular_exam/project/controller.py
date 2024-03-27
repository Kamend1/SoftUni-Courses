from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Food: Supply, Drink: Supply] = []

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def add_player(self, *args):
        added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        result = "Successfully added: " + ', '.join(added_players)
        return result

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):

        supply = self.__take_last_supply(sustenance_type)

        if supply:
            player = next(filter(lambda p: p.name == player_name, self.players), None)

            if player:
                if player.stamina == 100:
                    self.supplies.append(supply)
                    return f"{player_name} have enough stamina."

                else:
                    if player.stamina + supply.energy > 100:
                        player.stamina = 100
                    else:
                        player.stamina += supply.energy

                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        player_1 = next(filter(lambda p: p.name == first_player_name, self.players))
        player_2 = next(filter(lambda p: p.name == second_player_name, self.players))

        result = ""
        if player_1.stamina == 0:
            result += f"Player {first_player_name} does not have enough stamina."
        if player_2.stamina == 0:
            result += '\n' + f"Player {second_player_name} does not have enough stamina."

        if result:
            return result

        winner = None

        if player_1.stamina < player_2.stamina:
            if player_2.stamina - (player_1.stamina / 2) < 0:
                winner = player_1
                player_2.stamina = 0
            else:
                player_2.stamina -= (player_1.stamina / 2)

            if player_1.stamina - (player_2.stamina / 2) < 0:
                winner = player_2
                player_1.stamina = 0
            else:
                player_1.stamina -= (player_2.stamina / 2)

        else:
            if player_1.stamina - (player_2.stamina / 2) < 0:
                winner = player_2
                player_1.stamina = 0
            else:
                player_1.stamina -= (player_2.stamina / 2)

            if player_2.stamina - (player_1.stamina / 2) < 0:
                winner = player_1
                player_2.stamina = 0
            else:
                player_2.stamina -= (player_1.stamina / 2)

        if not winner:
            if player_1.stamina < player_2.stamina:
                winner = player_2
            else:
                winner = player_1

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - 2 * player.age < 0:
                player.stamina = 0
            else:
                player.stamina -= 2 * player.age

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    # def __str__(self):
    #     result = '\n'.join(str(player) for player in self.players)
    #     result += '\n' + '\n'.join(supply.details() for supply in self.supplies)
    #     return result

    # def __str__(self):
    #     info_string = ""
    #     for player in self.players:
    #         info_string += str(player) + "\n"
    #     for supply in self.supplies:
    #         info_string += supply.details() + "\n"
    #     return info_string.strip()

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info) + "\n"
        return result
