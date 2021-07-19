# Terminal shop app

> :information_source: Get sources with:
> ```bash
> git clone git@github.com:matbgn/terminal-shop.git
>```
 
> :fire: This app require python 3.6+

## Usage
Run app with:
```bash
cd terminal-shop
python app.py
```

## Class Diagram

```mermaid
classDiagram
    
    
 
    Order o-- Transaction
    
    Transaction o-- Item
    
    Item -- ItemRepository
    
    Order -- Controller
    
    App -- Router
    
    Router -- Controller
    Transaction -- Controller
    Controller -- Item
    
    Controller -- View
    class Router {
        -controller: Controller
        +run()
    }
    
    class Controller {
        -item_repository: ItemRepository
        -view: View
        -order: Order
        -transaction: Transaction = None
        +make_new_transaction()
        select_device()
        select_sim()
        select_case()
        select_charger()
        select_an_item(devices: List[Item], transaction_attribute: str)
        display_transaction_total(discount: float = 0.0)
        display_transaction_items()
        allow_discount()
        +display_order_total()
    }
    
    class Item {
        -code: String
        -category: String
        -description: String
        -price: int = 0
        +get_description()
        +get_category()
        +get_price()
    }
    
    class Order {
        -cart: Array<Transaction> = []
        -total: int = 0
        -discount: int = 0
        +get_cart()
        +set_cart(transaction: Transaction)
        +get_discount()
        +set_discount(value: float)
    }
    
    class Transaction {
        -device_type: Item = None
        -sim: Item = None
        -case: Item = None
        -chargers: Array<Item> = []
        -sub_total: int = 0
        +get_device_type()
        +set_device_type(value: Item)
        +get_sim()
        +set_sim(value: Item)
        +get_case()
        +set_case(value: Item)
        +get_chargers()
        +set_chargers(value: Item)
        +get_sub_total()
        +set_sub_total(value: float)
    }
    
    class ItemRepository {
        -path: str = "src/item_data.json"
        -items: Array<Item> = []
        load(path: str)
        add(item: Item)
        all()
        +find(index: int)
        +find_by_category(category: str)
    }
    
    class View {
        +print_void_line()$
        +display_single_item(cli: bool = False)$
        +display_items(items: List[Item])$
        +display_which_one_do_you_want(arg: str = "")$
        +display_you_selected()$
        +ask_for_device_type()
        +ask_for_a_valid_number(max_number: int)
        format_input_as_int(response: any)$
        +display_transaction_sub_total(transaction: Transaction, discount: float)$
        +display_transaction_items(transaction: Transaction)
        +ask_do_you_want_to_make_a_new_transaction()$
        +display_order_big_total(order: Order)$
    }
```

## Item Repository
> :bulb: Store in `item_data.json` and load with ItemRepository constructor

| Id | Category | Item code | Description                                  | Price ($) |
|----|----------|-----------|----------------------------------------------|-----------|
| 1  | Phone    | BPCM      | Compact                                      | 29.99     |
| 2  | Phone    | BPSH      | Clam shell                                   | 49.99     |
| 3  | Phone    | RPSS      | Robo phone - 5inch 64GB memory               | 199.99    |
| 4  | Phone    | RPLL      | Robo phone - 6inch 256GB memory              | 499.99    |
| 5  | Phone    | YPLS      | Y-phone standard 6 inch 64GB memory          | 549.99    |
| 6  | Phone    | YPLL      | Y-phone deluxe 6 inch 256GB memory           | 649.99    |
| 7  | Tablet   | RTMS      | RoboTab - 8 inch screen 64GB memory          | 149.99    |
| 8  | Tablet   | RTML      | RoboTab - 10 inch screen 128GB memory        | 299.99    |
| 9  | Tablet   | YTLM      | Y-tab standard - 10 inch screen 128GB memory | 499.99    |
| 10 | Tablet   | YTLL      | Y-tab deluxe - 10 inch screen 256GB memory   | 599.99    |
| 11 | SIM card | SMNO      | Sim free (no SIM card)                       | 0.00      |
| 12 | SIM card | SMPG      | Pay as you go (with SIM card)                | 9.99      |
| 13 | Case     | CSST      | Standard                                     | 0.00      |
| 14 | Case     | CSLX      | Luxury                                       | 50.00     |
| 15 | Charger  | CGCR      | Car                                          | 19.99     |
| 16 | Charger  | CGHM      | Home                                         | 15.99     |
                
**Grand-total = 3625.87**