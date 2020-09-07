
from abc import ABCMeta, abstractmethod


class BaseVehicle:
    """
    Base vehicle class
    """

    WEIGHT = 0
    PAYLOAD = 0
    FUEL_CONSUMPTION = 0
    SOUND = '...'

    def make_sound(self):
        print(self.SOUND)


class BaseCar(BaseVehicle, metaclass=ABCMeta):

    def __init__(self, vendor: str, model: str):
        self.vendor = vendor
        self.model = model

    @abstractmethod
    def ride(self, distance):
        pass


class BaseShip(BaseVehicle, metaclass=ABCMeta):

    def __init__(self, vendor: str, model: str, name: str):
        self.vendor = vendor
        self.model = model
        self.name = name

    @abstractmethod
    def sail(self, distance):
        pass



