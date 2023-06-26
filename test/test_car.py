import unittest
from datetime import datetime

from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tyre.carrigan import CarriganTyre
from tyre.octoprime import OctoprimeTyre

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_is_on=warning_light_on)
        self.assertFalse(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.strptime("2020-06-01", "%Y-%m-%d").date()
        last_service_date = datetime.strptime("2017-05-01", "%Y-%m-%d").date()
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.strptime("2020-04-01", "%Y-%m-%d").date()
        last_service_date = datetime.strptime("2017-05-01", "%Y-%m-%d").date()
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5) 
        battery = NubbinBattery(current_date=today, last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1) 
        battery = NubbinBattery(current_date=today, last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [0,0,0,0.9]
        tyre = CarriganTyre(wear_sensors)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.1,0.1,0.5,0.1]
        tyre = CarriganTyre(wear_sensors)
        self.assertFalse(tyre.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        wear_sensors = [1, 1, 0., 1]
        tyre = OctoprimeTyre(wear_sensors)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        wear_sensors = [0.1, 0.5, 0.5, 0.1]
        tyre = OctoprimeTyre(wear_sensors)
        self.assertFalse(tyre.needs_service())


if __name__ == '__main__':
    unittest.main()
