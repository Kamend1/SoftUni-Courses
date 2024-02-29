from project.car import Car
from project.cross_motorcycle import CrossMotorCycle
from project.family_car import FamilyCar
from project.motorcycle import MotorCycle
from project.race_motorcycle import RaceMotorCycle
from project.sport_car import SportCar
from project.vehicle import Vehicle

# moto_bmw = MotorCycle(30, 200)
# moto_bmw.drive(10)
# print(moto_bmw.fuel)
#
# moto_ducatti = RaceMotorCycle(10, 250)
# moto_ducatti.drive(2)
# print(moto_ducatti.fuel)
#
# ford = Car(45, 135)
# ford.drive(10)
# print(ford.fuel)
#
# vw_passat = FamilyCar(65, 190)
# vw_passat.drive(5)
# print(vw_passat.fuel)
#
# chevy_corvette = SportCar(89, 375)
# chevy_corvette.drive(5)
# print(chevy_corvette.fuel)

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
