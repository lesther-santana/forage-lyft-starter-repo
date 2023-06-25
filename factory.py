from car import Car
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery


class CarFactory():

    def create_calliope(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

    def create_glissade(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(
        current_date: datetime,
        last_service_date: datetime,
        warning_light_on: bool,
    ) -> Car:
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int        
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)