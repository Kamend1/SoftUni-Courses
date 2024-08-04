import os
import django
from django.db.models import Q, Count, Sum, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission


# Create queries within functions
def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    if search_string == "":
        astronauts = Astronaut.objects.all().order_by("name")

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    astronauts = Astronaut.objects.filter(query).order_by('name')

    result = []

    for a in astronauts:
        status = 'Active' if a.is_active else 'Inactive'
        result.append('Astronaut: ' + a.name + ', phone number: ' + a.phone_number + ', status: ' + status)

    return '\n'.join(result)


def get_top_astronaut():
    astronaut = Astronaut.objects.get_astronauts_by_missions_count().filter(num_missions__gt=0).first()

    if not astronaut:
        return "No data."

    return f"Top Astronaut: {astronaut.name} with {astronaut.num_missions} missions."


def get_top_commander():
    commander = Astronaut.objects.annotate(num_missions=Count('mission_commander')).filter(
        num_missions__gt=0).order_by('-num_missions', 'phone_number').first()

    if not commander:
        return "No data."

    return f"Top Commander: {commander.name} with {commander.num_missions} commanded missions."


def get_last_completed_mission():
    mission = Mission.objects.filter(
        status="Completed"
    ).prefetch_related('astronauts').annotate(num_spacewalks=Sum(
        'astronauts__spacewalks')).order_by('-launch_date').first()

    if not mission:
        return "No data."

    commander = mission.commander.name if mission.commander else 'TBA'
    astronaut_names = [a.name for a in mission.astronauts.all().order_by('name')]

    return 'The last completed mission is: ' + mission.name + '. Commander: ' + commander + '. Astronauts: '\
        + ', '.join(astronaut_names) + '. Spacecraft: ' + mission.spacecraft.name + '. Total spacewalks: ' \
        + str(mission.num_spacewalks) + '.'


def get_most_used_spacecraft():
    spacecraft = Spacecraft.objects.prefetch_related('missions', ).annotate(
        num_missions=Count('missions')).filter(num_missions__gt=0).order_by('-num_missions', 'name').first()

    if not spacecraft:
        return "No data."

    astronauts = Astronaut.objects.filter(missions_astronauts__spacecraft__name=spacecraft.name).distinct().count()

    return "The most used spacecraft is: " + spacecraft.name + ", manufactured by " + spacecraft.manufacturer + ", used in " + str(spacecraft.num_missions) + " missions, astronauts on missions: " + str(astronauts) + "."


def decrease_spacecrafts_weight():
    old_spacecrafts = Spacecraft.objects.prefetch_related(
        'missions').annotate(avg_weight=Avg('weight')).filter(
        missions__status="Planned", weight__gte=200).distinct().update(weight=F('weight') - 200)

    if old_spacecrafts == 0 or not Spacecraft.objects.all().exists():
        return "No changes in weight."
    else:
        spacecrafts = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))
        avg_weight = f"{spacecrafts['avg_weight']:.1f}"

        return "The weight of " + str(old_spacecrafts) \
            + " spacecrafts has been decreased. The new average weight of all spacecrafts is " + str(avg_weight) + "kg"


# astronaut1 = Astronaut.objects.create(
#     name='John Deer',
#     spacewalks=3,
#     phone_number='853967',
#     is_active=True,
#     date_of_birth='1980-01-01',
# )
#
# astronaut2 = Astronaut.objects.create(
#     name='Jane Smith',
#     spacewalks=1,
#     phone_number='123456',
#     is_active=True,
#     date_of_birth='1985-05-15',
# )
#
# astronaut3 = Astronaut.objects.create(
#     name='Josie Stamp',
#     spacewalks=0,
#     phone_number='111111',
#     is_active=False,
#     date_of_birth='1990-03-12',
# )

# spacecraft1 = Spacecraft.objects.create(
#     name="Explorer I",
#     manufacturer='SpaceTech Inc.',
#     capacity=5,
#     launch_date= '2022-01-01',
#     weight=12000.5,
# )
#
# spacecraft2 = Spacecraft.objects.create(
#     name="Explorer II",
#     manufacturer='SpaceX',
#     capacity=2,
#     launch_date= '2023-05-01',
#     weight=10000.2,
# )
print(get_last_completed_mission())