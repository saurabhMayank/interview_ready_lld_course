import uuid
from enum import Enum


class Cart:
    """
    Cart class defining the cart
    """
    def __init__(self):
        self.item_list = []


    def get_items_list(self):
        return self.item_list
    
    def add_item(self, item):
        self.item_list.append(item)


class Order:
    """
    Class for Order
    """
    def __init__(self, item_list: list):
        self.item_list = item_list
        self.order_id = uuid.uuid4()

class Payment:
    """
    Class for Payments -> where different methods can be passed
    based on which transaction of order is met
    """
    def __init__(self):
        self.payment_id = uuid.uuid5()
        self.payment_method = PaymentMethod()

class PaymentMethods(Enum):
    """
    Enum contaning all the payment methods possible
    """
    UPI, CASH, CC, NETBANKING = 1, 2, 3, 4




class Customer:
    """
    Customer Class -> Containing all the data members and variable functions
    of the customer class
    """
    cart = Cart()
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def return_item():
        pass

    
    def view_item(self, name: str):
        item = Item(name)
        return item.get_item()

    def buy_item(self):
        pass

    def add_to_cart(self, item):
        cart.add_item(item)

    def view_items_in_cart(self) -> list:
        """
        Giving back the list of items in the cart
        """
        return cart.get_items_list()

    def checkout(self):
        # convert items of cart into order
        items_list = cart.get_items_list()
        order = Order(items_list)


    



class Product:
    """
    Class Defining a Product.
    Ex -> Earphone is a product. Lot of items can be an earphone
    """
    def __init__(self, name: str, product_id=""):
        self.product_id = product_id
        self.name = name
    
    def generate_id(self):
        self.product_id = uuid.uuid4()





class Item(Product):
    """
    Item Class defining a single item
    """
    def __init__(self, price=""):
        self.price = price
    
    def set_price(self, price: str):
        self.price = price
    
    def get_price(self):
        return self.price
    
    def get_item(self) -> dict:
        return {"name": self.name, "price": self.price}
    

if __name__ == "__main__":
    customer = Customer("mayank", "memayank9@gmail.com")
    customer_id = customer.generate_id()
    # item price set by admin -> which is out of scope from this code
    item_1 = Item("shampoo")
    item_2 = Item("oil")
    
    cart = Cart(customer_id)
