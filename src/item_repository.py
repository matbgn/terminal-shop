import json
from typing import List

from src.item import Item


class ItemRepository:
    def __init__(self, path: str = "src/item_data.json") -> None:
        """Initialize items DB"""
        self.__items = []
        self.__load(path)

    def __load(self, path: str) -> None:
        """Load source data in format JSON"""
        with open(path) as source_file:
            source_data = json.load(source_file)

        for i in range(len(source_data)):
            item = Item(source_data[i]['item_code'],
                        source_data[i]['category'],
                        source_data[i]['description'],
                        source_data[i]['price'])
            self.__add(item)

    def __add(self, item: Item) -> None:
        """Add a new item to items DB"""
        self.__items.append(item)

    def __all(self) -> List[Item]:
        """Returns all items objects from DB"""
        return self.__items

    def find(self, index: int) -> Item:
        """Return the ith item object from DB"""
        return self.__all()[index]

    def find_by_category(self, category: str) -> List[Item]:
        """Return a list of corresponding items"""
        result = []
        for i in self.__all():
            result.append(i) if i.category == category else None

        return result

