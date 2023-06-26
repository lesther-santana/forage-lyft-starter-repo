from .battery import Battery
from datetime import date


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 4)
        return service_threshold_date < self.__current_date
