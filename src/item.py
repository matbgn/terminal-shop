class Item:
    def __init__(self, code: str, category: str, description: str, price: int = 0) -> None:
        self.__code = code
        self.__category = category
        self.__description = description
        self.__price = price

    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def category(self) -> str:
        return self.__category.capitalize().replace('_', ' ')

    @property
    def price(self) -> float:
        return self.__price
