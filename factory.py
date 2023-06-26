from car import Car
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from tyre.carrigan import CarriganTyre
from tyre.octoprime import OctoprimeTyre


class CarFactory:

    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        wear_sensors: list[float],
        tyre_type: str
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        if tyre_type == "carrigan":
            tyre = CarriganTyre(wear_sensors)
        elif tyre_type == "octoprime":
            tyre = OctoprimeTyre(wear_sensors)
        return Car(engine=engine, battery=battery, tyre=tyre)

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        wear_sensors: list[float],
        tyre_type: str
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        if tyre_type == "carrigan":
            tyre = CarriganTyre(wear_sensors)
        elif tyre_type == "octoprime":
            tyre = OctoprimeTyre(wear_sensors)
        return Car(engine=engine, battery=battery, tyre=tyre)

    @staticmethod
    def create_palindrome(
        current_date: date,
        last_service_date: date,
        warning_light_on: bool,
        wear_sensors: list[float],
        tyre_type: str
    ) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        if tyre_type == "carrigan":
            tyre = CarriganTyre(wear_sensors)
        elif tyre_type == "octoprime":
            tyre = OctoprimeTyre(wear_sensors)
        return Car(engine=engine, battery=battery, tyre=tyre)
    
    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        wear_sensors: list[float],
        tyre_type: str        
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        if tyre_type == "carrigan":
            tyre = CarriganTyre(wear_sensors)
        elif tyre_type == "octoprime":
            tyre = OctoprimeTyre(wear_sensors)
        return Car(engine=engine, battery=battery, tyre=tyre)

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        wear_sensors: list[float],
        tyre_type: str
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        if tyre_type == "carrigan":
            tyre = CarriganTyre(wear_sensors)
        elif tyre_type == "octoprime":
            tyre = OctoprimeTyre(wear_sensors)
        return Car(engine=engine, battery=battery, tyre=tyre)