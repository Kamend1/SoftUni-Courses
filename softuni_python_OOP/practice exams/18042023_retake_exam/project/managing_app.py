from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    ALLOWED_VEHICLE_TYPES = ['CargoVan', 'PassengerCar']
    # ROUTE_ID = 1

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[PassengerCar: BaseVehicle, CargoVan: BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users), None)

        if user:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in self.ALLOWED_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        vehicle_object = globals()[vehicle_type]
        vehicle = vehicle_object(brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:

                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                else:
                    route.is_locked = True
        else:
            new_route = Route(start_point, end_point, length, len(self.routes) + 1)
            self.routes.append(new_route)
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."


    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool):

        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            user.decrease_rating()
            vehicle.change_status()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):


        sorted_vehicles = sorted(self.vehicles, key=lambda v: (v.brand, v.model))
        vehicles_for_repair = [vehicle for vehicle in sorted_vehicles if vehicle.is_damaged]

        if len(vehicles_for_repair) <= count:

            for vehicle in vehicles_for_repair:
                vehicle.is_damaged = False
                vehicle.recharge()

            return f"{len(vehicles_for_repair)} vehicles were successfully repaired!"

        else:

            for idx in range(count):
                current_vehicle = vehicles_for_repair[idx]
                current_vehicle.is_damaged = False
                current_vehicle.recharge()

            return f"{count} vehicles were successfully repaired!"

    def users_report(self):

        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result = "*** E-Drive-Rent ***\n"
        result += '\n'.join(str(user) for user in sorted_users)

        return result
