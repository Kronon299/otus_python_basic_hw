from base import BaseShip


class FerryBoat(BaseShip):

    WEIGHT = 20000
    PAYLOAD = 10000
    FUEL_CONSUMPTION = 10
    MAX_FUEL = 6000

    def __init__(self, *args, fuel=MAX_FUEL, **kwargs):
        super().__init__(*args, **kwargs)
        self.__fuel = fuel
        print(f"Created {self.__str__()}.")

    def __str__(self):
        return f"{self.__class__.__name__} {self.vendor} {self.model} named {self.name} with {self.fuel} of fuel"

    def __repr__(self):
        return str(self)

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            self.__fuel = 0
        else:
            self.__fuel = value

    def sail(self, distance: int) -> None:
        fuel_to_spend = distance * self.FUEL_CONSUMPTION
        if fuel_to_spend > self.fuel:
            print(f"Cannot go, not enough fuel {self.fuel}, need {fuel_to_spend}")
            return
        self.fuel -= fuel_to_spend
        print(f"Going {distance} units. Was spent {fuel_to_spend} of fuel, left {self.fuel} of fuel")

    def add_fuel(self, value):
        print("Adding", value, "of fuel")
        self.fuel += value
        if self.fuel > self.MAX_FUEL:
            print("lost", self.fuel - self.MAX_FUEL, "of fuel")
            self.fuel = self.MAX_FUEL
        return self.fuel
