class PositiveValueError(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} less than 0."


class LowFuelError(ValueError):
    pass

