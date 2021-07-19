from typing import List

from src.item import Item
from src.order import Order
from src.transaction import Transaction


class View:
    @staticmethod
    def print_void_line():
        """Print a single empty line"""
        print()

    @staticmethod
    def display_single_item(item, cli: bool = False):
        """Single line formatting for displaying an item"""
        if hasattr(item, "category"):
            msg = f'{item.category} - {item.description} ({item.price:.2f}$)'
        else:
            msg = "No item"
        return msg if cli else print(msg)

    @staticmethod
    def display_items(items: List[Item]):
        """Display all items"""
        count = 1
        for i in items:
            print(f'[{count}] {i.category} - {i.description} ({i.price:.2f}$)')
            count = count + 1

    @staticmethod
    def display_which_one_do_you_want(arg: str = "") -> None:
        print("Which one do you want?") if arg == "" else print(f"Which {arg} do you want?")

    @staticmethod
    def display_you_selected() -> None:
        print("You selected:")

    def ask_for_device_type(self) -> str:
        """Ask which device is wanted and return its value"""
        print("Which device do you want: \n[1] Phone \n[2] Tablet")
        response = self.ask_for_a_valid_number(2)
        return "Phone" if response == 1 else "Tablet"

    def ask_for_a_valid_number(self, max_number: int) -> int:
        response = input("Enter your number and press enter: ")
        response = self.format_input_as_int(response)

        while type(response) != int or (response < 0 or response > max_number):
            response = input("Enter a valid number and press enter: ")
            response = self.format_input_as_int(response)

        print()
        return response

    @staticmethod
    def format_input_as_int(response: any):
        try:
            return int(response)
        except ValueError:
            return -1

    @staticmethod
    def display_transaction_sub_total(transaction: Transaction, discount: float) -> None:
        if discount < 0.01:
            print(f'Your actual transaction sub-total is: {transaction.sub_total:.2f}$')
        else:
            print(f'Your actual transaction sub-total is: {transaction.sub_total:.2f}$\n'
                  f'You received a 10% discount off the price of the actual device\n'
                  f'The amount of money saved is: {discount:.2f}$')
        print()

    def display_transaction_items(self, transaction: Transaction) -> None:
        print(f'You\'re actual transaction is composed by:\n'
              f'- Device: {self.display_single_item(transaction.device_type, True)}\n'
              f'- SIM Card: {self.display_single_item(transaction.sim, True)}\n'
              f'- Case: {self.display_single_item(transaction.case, True)}\n'
              f'- Charger(s): {self.display_single_item(transaction.chargers, True)}'
              )

    @staticmethod
    def ask_do_you_want_to_make_a_new_transaction() -> bool:
        response = input("Do you want to make a new transaction? [Y]es or [N]o: ")

        while response != "N" and response != "n" and response != "Y" and response != "y":
            response = input("Enter a valid response, either Y/y for Yes or N/n for No and press enter: ")

        print()
        return True if response == "Y" or response == "y" else False

    @staticmethod
    def display_order_big_total(order: Order) -> None:
        big_total = 0
        for i in order.cart:
            big_total = big_total + i.sub_total
        if order.discount < 0.01:
            print(f'Your cart amount is: {big_total:.2f}$')
        else:
            print(f'Your cart amount is: {big_total:.2f}$\n'
                  f'You received a 10% discount on one or multiple devices\n'
                  f'The total amount of money saved is: {order.discount:.2f}$')
        print()
