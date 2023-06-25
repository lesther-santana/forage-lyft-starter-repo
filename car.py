from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.__engine = engine
        self.__battery = battery

    def needs_service(self) -> bool:
        return self.__engine.needs_service() or self.__battery.needs_service()
