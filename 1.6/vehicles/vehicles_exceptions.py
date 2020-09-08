class PositiveValueError(ValueError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} less than 0."


class LowFuelError(ValueError):
    def __init__(self, present_value, need_value):
        self.present_value = present_value
        self.need_value = need_value

    def __str__(self):
        return f"{self.present_value} fuel is not enough, {self.need_value} is needed."

