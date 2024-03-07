from project.room import Room

class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.guests = 0
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return

        people = room.guests
        result = room.free_room()

        if not result:
            room.guests -= people
    def status(self):
        result = "Hotel " + self.name + " has " + str(self.guests) + " total guests"
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        result += "\nFree rooms: "+', '.join(str(x) for x in free_rooms)
        result += "\nTaken rooms: " + ', '.join(str(x) for x in taken_rooms)

        return result




