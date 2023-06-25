from .engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self) -> bool:
        return self.warning_light_is_on