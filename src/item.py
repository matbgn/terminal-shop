from abc import ABCMeta, abstractmethod


class Item:
    def __init__(self, code: str, category: str, description: str, price: int):
        self.code = code
        self.category = category
        self.description = description
        self.price = price


class Device(Item):
    pass


class Sim(Item):
    pass


class Case(Item):
    pass


class Charger(Item):
    pass
