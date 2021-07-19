from src.item_repository import ItemRepository
from src.order import Order
from src.controller import Controller
from src.router import Router
from src.view import View

# Bootstrap entire application
controller = Controller(ItemRepository(), View(), Order())
router = Router(controller)
router.run()
