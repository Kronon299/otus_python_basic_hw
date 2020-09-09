from base import BaseCar
from vehicles_exceptions import LowFuelError
from parts import Engine, base_engine, sport_engine, base_horn


class PassengerCar(BaseCar):
    """Class for passenger cars"""

    WEIGHT = 3000
    PAYLOAD = 1000
    FUEL_CONSUMPTION = 1
    MAX_FUEL = 750
    engine = base_engine
    horn = base_horn

    def __init__(self, *args, fuel=MAX_FUEL, **kwargs):
        super().__init__(*args, **kwargs)
        self.__fuel = fuel
        print(f"Created {self.__str__()}.")

    def __str__(self):
        return f"{self.__class__.__name__} {self.vendor} {self.model} with {self.fuel} of fuel"

    def __repr__(self):
        return str(self)

    def make_sound(self):
        print(self.horn.sound)

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            self.__fuel = 0
        else:
            self.__fuel = value

    def ride(self, distance: int) -> None:
        try:
            fuel_to_spend = distance * self.FUEL_CONSUMPTION * self.engine.consumption_index
            if fuel_to_spend > self.fuel:
                raise LowFuelError(self.fuel, fuel_to_spend)
            self.fuel -= fuel_to_spend
            real_speed = self.engine.real_speed(self.PAYLOAD)
            print(f"Going {distance} units. Was spent {fuel_to_spend} of fuel, left {self.fuel} of fuel. \n"
                  f"Speed: {real_speed}.\n"
                  f"Journey takes {distance/real_speed} hours.")
        except LowFuelError as err:
            print(f"Can't go. Fuel: {err.args[0]}, need {err.args[1]}")

    def add_fuel(self, value):
        print("Adding", value, "of fuel")
        self.fuel += value
        if self.fuel > self.MAX_FUEL:
            print("lost", self.fuel - self.MAX_FUEL, "of fuel")
            self.fuel = self.MAX_FUEL
        return self.fuel

    def set_engine(self, obj=None, *args, **kwargs):
        if not obj:
            self.engine = Engine(*args, **kwargs)
        else:
            self.engine = obj


if __name__ == '__main__':
    car = PassengerCar('Opel', 'Astra')
    car.make_sound()
    print("car.fuel: ", car.fuel)
    car.add_fuel(-600)
    print("car.fuel: ", car.fuel)
    car.add_fuel(650)
    print("car.fuel: ", car.fuel)
    car.ride(500)
    car.set_engine(sport_engine)
    print(car.engine)
    car.add_fuel(750)
    car.ride(500)
