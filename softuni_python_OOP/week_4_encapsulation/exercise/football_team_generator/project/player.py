class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        result = "Player: " + self.name + "\n" + \
                 "Sprint: " + str(self.__sprint) + "\n" + \
                 "Dribble: " + str(self.__dribble) + "\n" + \
                 "Passing: " + str(self.__passing) + "\n" + \
                 "Shooting: " + str(self.__shooting)

        return result
