from project.rooms.room import Room


class AloneOld(Room):
    DEFAULT_MEMBERS = 1
    DEFAULT_ROOM_COST = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.DEFAULT_MEMBERS)
        self.room_cost = self.DEFAULT_ROOM_COST
