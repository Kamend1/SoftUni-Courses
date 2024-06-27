import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character, CharClassChoices


# Create queries within functions
def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    new_artifact = Artifact(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    new_artifact.save()

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.age > 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    artifacts = Artifact.objects.all()
    artifacts.delete()


def add_locations():
    Location.objects.create(
        name='Sofia',
        region='Sofia Region',
        population=1329000,
        description='The capital of Bulgaria and the largest city in the country',
        is_capital=False,
    )

    Location.objects.create(
        name='Plovdiv',
        region='Plovdiv Region',
        population=346942,
        description='The second-largest city in Bulgaria with a rich historical heritage',
        is_capital=False,
    )

    Location.objects.create(
        name='Varna',
        region='Varna Region',
        population=330486,
        description='A city known for its sea breeze and beautiful beaches on the Black Sea',
        is_capital=False,
    )


def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    result = []

    for location in locations:
        result.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(result)


def new_capital():
    new_capital = Location.objects.first()
    new_capital.is_capital = True
    new_capital.save()


def get_capitals():
    capitals = Location.objects.values('name').filter(is_capital=True)
    return capitals


def delete_first_location():
    Location.objects.first().delete()


def add_cars():
    new_car1 = Car(
        model='Mercedes C63 AMG',
        year=2019,
        color='white',
        price='120000.00',
    )
    new_car1.save()

    new_car2 = Car(
        model='Audi Q7 S line',
        year=2023,
        color='black',
        price='183900.00',
    )
    new_car2.save()

    new_car3 = Car(
        model='Chevrolet Corvette',
        year=2021,
        color='dark grey',
        price='199999.00',
    )
    new_car3.save()


def apply_discount():

    cars = Car.objects.all()
    for car in cars:
        discount = 1 - sum([int(char) for char in str(car.year)]) / 100
        car.price_with_discount = float(car.price) * discount

    Car.objects.bulk_update(cars, ['price_with_discount'])


def get_recent_cars():
    cars = Car.objects.values('model', 'price_with_discount').filter(year__gt=2020)
    return cars


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():

    result = []
    unfinished_tasks = Task.objects.filter(is_finished=False)

    for task in unfinished_tasks:
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return '\n'.join(result)


def complete_odd_tasks():

    all_tasks = Task.objects.all()

    for task in all_tasks:
        if task.id % 2 != 0:
            task.is_finished = True

    Task.objects.bulk_update(all_tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):

    deciphered_text = ""
    for char in text:
        new_char = chr(ord(char) - 3)
        deciphered_text += new_char

    Task.objects.filter(title=task_title).update(description=deciphered_text)

    # all_tasks = Task.objects.filter(title=task_title)
    # for task in all_tasks:
    #     task.description = deciphered_text
    #
    # Task.objects.bulk_update(all_tasks, ['description'])


def add_rooms():
    HotelRoom.objects.create(
        room_number=401,
        room_type='Standard',
        capacity=2,
        amenities='Tv',
        price_per_night=100
    )

    HotelRoom.objects.create(
        room_number=501,
        room_type='Deluxe',
        capacity=3,
        amenities='Wi-Fi',
        price_per_night=200
    )

    HotelRoom.objects.create(
        room_number=601,
        room_type='Deluxe',
        capacity=6,
        amenities='Jacuzzi',
        price_per_night=400
    )


def get_deluxe_rooms():
    all_deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    result = []

    for room in all_deluxe_rooms:
        if room.id % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return '\n'.join(result)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all()

    for idx in range(len(all_rooms)):
        if idx == 0 and all_rooms[0].is_reserved:
            all_rooms[idx].capacity += all_rooms[idx].id
        elif idx != 0 and all_rooms[idx].is_reserved:
            all_rooms[idx].capacity += all_rooms[idx-1].capacity

    HotelRoom.objects.bulk_update(all_rooms, ['capacity'])


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if not last_room.is_reserved:
        last_room.delete()


def update_characters():

    # characters_all = Character.objects.all()
    #
    # for character in characters_all:
    #     if character.class_name == 'Mage':
    #         character.level += 3
    #         if character.intelligence >= 8:
    #             character.intelligence -= 7
    #         else:
    #             character.intelligence = 1
    #     elif character.class_name == 'Warrior':
    #         if int(character.hit_points * 0.5) == 0:
    #             character.hit_points = 1
    #         else:
    #             character.hit_points = int(character.hit_points * 0.5)
    #         character.dexterity += 4
    #     elif character.class_name in ["Assassin", "Scout"]:
    #         character.inventory = "The inventory is empty"
    #
    #     character.save()

    Character.objects.filter(class_name="Mage").update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name="Warrior").update(
        hit_points=F('hit_points') // 2,
        dexterity=F('dexterity') + 4
    )

    # Update Scout and Assassin characters
    Character.objects.filter(class_name__in=["Scout", "Assassin"]).update(
        inventory="The inventory is empty"
    )


def fuse_characters(first_character: Character, second_character: Character):
    if not hasattr(CharClassChoices, 'FUSION'):
        CharClassChoices.FUSION = 'Fusion'
        CharClassChoices.choices += (('Fusion', 'Fusion'),)

    new_inventory = 'The inventory is empty'

    if first_character.class_name in ["Mage", "Scout"]:
        new_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    elif first_character.class_name in ["Warrior", "Assassin"]:
        new_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=int((first_character.level + second_character.level) // 2),
        strength=int((first_character.strength + second_character.strength) * 1.2),
        dexterity=int((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=int((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory=new_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()

# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


# print(create_artifact('Ancient Sword',
#                       'Lost Kingdom',
#                       500,
#                       'A legendary sword with a rich history',
#                       True))
# print(create_artifact('Crystal Amulet',
#                       'Mystic Forest',
#                       300,
#                       'A magical amulet believed to bring good fortune',
#                       True))
# print(create_artifact('Stone Tablet',
#                       'Ruined Temple',
#                       1000,
#                       'An ancient tablet covered in mysterious inscriptions', False))
#
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)

# add_locations()

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

# add_cars()

# apply_discount()
# print(get_recent_cars())

# add_rooms()

# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=401).is_reserved)

# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)

# update_characters()
