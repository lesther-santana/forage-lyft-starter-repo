from .engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
