from src.controller import Controller


class Router:
    def __init__(self, controller: Controller):
        self.__controller = controller

    def run(self):
        print("Welcome to our terminal shop app!\n"
              "You will be guided throughout your purchases\n"
              "Compose your cart with nice transactions bundles\n"
              "Enjoy your journey!\n")

        trigger = True
        while trigger:
            trigger = self.__controller.make_new_transaction()
            self.__controller.display_order_total()

        print("Thank you in advance for your payment and have a great day!")
