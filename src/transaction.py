from typing import List

from src.item import Item


class Transaction:
    def __init__(self, device_type: Item = None, sim: Item = None,
                 case: Item = None, chargers: List[Item] = [], sub_total: int = 0) -> None:
        self.__device_type = device_type
        self.__sim = sim
        self.__case = case
        self.__chargers = chargers
        self.__sub_total = sub_total

    @property
    def device_type(self):
        return self.__device_type

    @device_type.setter
    def device_type(self, value: Item):
        self.__device_type = value
        self.__sub_total = self.__sub_total + value.price

    @property
    def sub_total(self):
        return self.__sub_total

    @sub_total.setter
    def sub_total(self, value: float):
        self.__sub_total = value

    @property
    def sim(self):
        return self.__sim

    @sim.setter
    def sim(self, value: Item):
        self.__sim = value
        self.__sub_total = self.__sub_total + value.price

    @property
    def case(self):
        return self.__case

    @case.setter
    def case(self, value: Item):
        self.__case = value
        self.__sub_total = self.__sub_total + value.price

    @property
    def chargers(self):
        return self.__chargers

    @chargers.setter
    def chargers(self, value: Item):
        self.__chargers = value
        self.__sub_total = self.__sub_total + value.price
