from typing import List

from src.transaction import Transaction


class Order:
    def __init__(self, cart: List[Transaction] = [], total: int = 0,
                 discount: int = 0) -> None:
        self.__cart = cart
        self.__total = total
        self.__discount = discount

    @property
    def cart(self):
        return self.__cart

    @cart.setter
    def cart(self, transaction: Transaction):
        self.__cart.append(transaction)

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value: float):
        self.__discount = value
