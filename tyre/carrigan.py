from tyre import Tyre
class CarriganTyre(Tyre):

    def __init__(self, wear_sensors: list[float]) -> None:
        self.wear_sensors = wear_sensors
    
    def needs_service(self):
        threshold = 0.9
        return sum(self.wear_sensors) >= threshold

        