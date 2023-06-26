from tyre import Tyre
class OctoprimeTyre(Tyre):

    def __init__(self, wear_sensors: list[float]) -> None:
        self.wear_sensors = wear_sensors
    
    def needs_service(self):
        threshold = 3
        return sum(self.wear_sensors) >= threshold