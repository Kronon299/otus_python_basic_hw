from base import BaseShip
from vehicles_exceptions import LowFuelError, PositiveValueError


class FerryBoat(BaseShip):

    WEIGHT = 20000
    PAYLOAD = 10000
    FUEL_CONSUMPTION = 10
    MAX_FUEL = 6000
    __consumption_index = 1
    cargo = 0

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
        try:
            fuel_to_spend = distance * self.FUEL_CONSUMPTION * self.__consumption_index
            if fuel_to_spend > self.fuel:
                raise LowFuelError(self.fuel, fuel_to_spend)
            self.fuel -= fuel_to_spend
            print(f"Going {distance} units. Was spent {fuel_to_spend} of fuel, left {self.fuel} of fuel")
        except LowFuelError as err:
            print(f"Can't go. Fuel: {err.args[0]}, need {err.args[1]}")

    def add_fuel(self, value):
        print("Adding", value, "of fuel")
        self.fuel += value
        if self.fuel > self.MAX_FUEL:
            print("lost", self.fuel - self.MAX_FUEL, "of fuel")
            self.fuel = self.MAX_FUEL
        return self.fuel

    def bring_cargo(self, cargo: int):
        try:
            self.cargo += cargo
            if self.cargo < 0:
                raise PositiveValueError(self.cargo)
            if self.cargo > self.PAYLOAD:
                print("can't bring so heavy cargo!")
                return
            print(f'Bringing {cargo} on board. Total cargo: {self.cargo}')
            self.__consumption_index += 0.001 * cargo
        except PositiveValueError as err:
            self.cargo = 0
            print(err.__str__())

    def offload(self):
        print(f'{self.name} was offloaded')
        self.cargo = 0
        self.__consumption_index = 1


if __name__ == '__main__':
    ship = FerryBoat('Syma', 'Black Stealth', 'Queen')
    ship.make_sound()
    print("ship.fuel: ", ship.fuel)
    ship.add_fuel(-600)
    print("ship.fuel: ", ship.fuel)
    ship.add_fuel(550)
    print("ship.fuel: ", ship.fuel)
    ship.sail(2500)
    print(ship._FerryBoat__consumption_index)
    ship.bring_cargo(-5000)
    print(f"ship.cargo: {ship.cargo}, consumption index: {ship._FerryBoat__consumption_index}")
    ship.offload()
    print(f"ship.cargo: {ship.cargo}, consumption index: {ship._FerryBoat__consumption_index}")
