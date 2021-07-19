from typing import List

from src.item_repository import ItemRepository
from src.item import Item
from src.order import Order
from src.transaction import Transaction
from src.view import View


class Controller:
    def __init__(self, item_repository: ItemRepository, view: View, order: Order):
        self.__item_repository = item_repository
        self.__view = view
        self.__transaction = None
        self.__order = order

    def make_new_transaction(self):
        self.__transaction = Transaction()
        self.__select_sim() if self.__select_device() else None
        self.__select_case()
        self.__select_charger()

        self.__order.cart = self.__transaction
        self.__display_transaction_items()
        if self.__allow_discount():
            discount = self.__transaction.device_type.price * 0.1
            self.__transaction.sub_total = self.__transaction.sub_total - discount
            self.__order.discount = self.__order.discount + discount
            self.__display_transaction_total(discount)
        else:
            self.__display_transaction_total()

        self.__transaction = Transaction()
        return self.__view.ask_do_you_want_to_make_a_new_transaction()

    def __select_device(self) -> int:
        # 1 - Ask user which type of device he want
        device = self.__view.ask_for_device_type()
        # 2 - Ask repo for specific device list
        devices = self.__item_repository.find_by_category(device)
        # 3 - Display "Which one do you want?"
        self.__view.display_which_one_do_you_want()
        # 4 - Proceed to standard selection
        self.__select_an_item(devices, "device_type")
        return 1 if device == "Phone" else 0

    def __select_sim(self) -> None:
        # 1 - Display "Which one do you want?"
        self.__view.display_which_one_do_you_want("SIM card")
        # 2 - Ask repo for specific device list
        devices = self.__item_repository.find_by_category("Sim card")
        # 3 - Proceed to standard selection
        self.__select_an_item(devices, "sim")

    def __select_case(self) -> None:
        # 1 - Display "Which one do you want?"
        self.__view.display_which_one_do_you_want("case")
        # 2 - Ask repo for specific device list
        devices = self.__item_repository.find_by_category("Case")
        # 3 - Proceed to standard selection
        self.__select_an_item(devices, "case")

    def __select_charger(self) -> None:
        # 1 - Display "Which one do you want?"
        self.__view.display_which_one_do_you_want("charger")
        # 2 - Ask repo for specific device list
        devices = self.__item_repository.find_by_category("Charger")
        # 3 - Append "both" possibilities
        both_total = 0
        both_description = ""
        for i in self.__item_repository.find_by_category("Charger"):
            both_total = both_total + i.price
            both_description = both_description + i.description + " & "
        devices.append(Item("BOTH", "charger", f"Both {both_description[:len(both_description)-3]}", both_total))
        # 4 - Append "none" possibility
        devices.append(Item("NONE", "charger", "None"))
        # 5 - Proceed to standard selection
        self.__select_an_item(devices, "chargers")

    def __select_an_item(self, devices: List[Item], transaction_attribute: str) -> None:
        self.__view.display_items(devices)
        # 4 - Ask for corresponding number
        choice_index = self.__view.ask_for_a_valid_number(len(devices)) - 1
        # 5 - Store choice
        setattr(self.__transaction, transaction_attribute, devices[choice_index])
        # 6 - Display selected choice
        self.__view.display_you_selected()
        self.__view.display_single_item(getattr(self.__transaction, transaction_attribute))
        self.__view.print_void_line()

    def __display_transaction_total(self, discount: float = 0.0) -> None:
        self.__view.display_transaction_sub_total(self.__transaction, discount)

    def __display_transaction_items(self) -> None:
        self.__view.display_transaction_items(self.__transaction)

    def __allow_discount(self) -> bool:
        return True if len(self.__order.cart) > 1 else False

    def display_order_total(self) -> None:
        self.__view.display_order_big_total(self.__order)
