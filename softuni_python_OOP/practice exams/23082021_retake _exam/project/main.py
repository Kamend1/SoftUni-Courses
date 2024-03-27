from project.planet.planet_repository import PlanetRepository
from project.space_station import SpaceStation

ss = SpaceStation()
pr = PlanetRepository
print(ss.add_astronaut("Biologist", "Peter"))
# print(ss.add_astronaut("Biologist", "Peter"))
# print(ss.add_astronaut("Biologist", "Mitko"))
# print(ss.add_astronaut("Geodesist", "Tosho"))
# print(ss.add_astronaut("Geodesist", "Pesho"))
# print(ss.add_astronaut("Geodesist", "Lilly"))
# print(ss.add_astronaut("Meteorologist", "Gosho"))
# print(ss.add_astronaut("Meteorologist", "Nasko"))
# print(ss.add_astronaut("Meteorologist", "Ivan"))
print(ss.add_astronaut("Meteorologist", "Retired"))

# print(ss.astronauts.astronauts[0])
# for astronaut in ss.astronauts.astronauts:
#     print(astronaut)
ss.recharge_oxygen()
# for astronaut in ss.astronauts.astronauts:
#     print(astronaut)
print(ss.retire_astronaut("Retired"))
# print(ss.retire_astronaut("Retired"))
print(ss.add_planet("Earth", "mineral_1, mineral_2, mineral_3, mineral_4, mineral_5, mineral_6, mineral_7, mineral_8"))
print(ss.add_planet("Earth", "mineral_1, mineral_2, mineral_3, mineral_4, mineral_5, mineral_6, mineral_7, mineral_8"))
print(ss.add_planet("Earth", "mineral_1, mineral_2, mineral_3, mineral_4, mineral_5, mineral_6, mineral_7, mineral_8"))
print(ss.add_planet("Venera", "i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9, i_10, i_11, i_12, i_13, i_14, i_15"))
print(ss.add_planet("Mars", "p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15"))
# print(ss.add_planet(" ", "mineral_1, mineral_2, mineral_3, mineral_4, mineral_5, mineral_6, mineral_7, mineral_8"))
print(ss.planet_repository.planets[0].items)
# print(ss.send_on_mission("Earth"))
# print(ss.send_on_mission("Venera"))
# print(ss.send_on_mission("Mars"))
print(ss.planet_repository.planets[2].items)
print(ss.report())