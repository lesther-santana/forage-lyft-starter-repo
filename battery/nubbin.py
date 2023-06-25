from .battery import Battery
from datetime import datetime, timedelta


class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_time = timedelta(days=365*4)
        time_difference = self.__current_date - self.__last_service_date
        return time_difference >= service_threshold_time
