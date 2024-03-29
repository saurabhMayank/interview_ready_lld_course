"""
completed till 5 mins of code part 2
"""


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


class OrderDetails:
    """
    Basic Details of the Order common to all types of order so it can be used in
    different classes
    One method could more be done was
    => Making a abstractclass called OrderType
    => Then inherting Order and ReturnOrder from OrderType
    => Using the abstract ParentClass OrderType wherever needed and on runtime
    => Pass the appropriate run time class

    But this will pose the problem of Fat Interfaces. Too much details 
    will be passed using the instance in other classes such as delivery class which is not needed
    Interface segragation principle of Solid principle aims to avoid passing too much details
    to another classes which is not needed
    """
    def __init__(self, source_add, destination_add):
        self.order_id = uuid.uuid4()
        self.source_address = source_add
        self.destination_address = destination_add

class Order:
    """
    Class for Order
    """
    def __init__(self, item_list, source_add, destination_add):
        self.order_details = OrderDetails(source_add, destination_add)
        self.source_add = source_add
        self.amount = self.total_amount(item_list)
        self.order_status = OrderStatus
        self.deliveries = [] # a single order has list of deliveries
        self.invoices = [] # store all the invoices for the order
    
    def total_amount(self, item_list):
        """
        Returning the total amount of the order
        """
        amount = 0
        for item in item_list:
            amount = amount+item.get_price()
        
        return amount
    
    
    def status_change(self, order_status):
        """
        Listener for status change. If status change is payment_complete
        then initiate delivery
        Observer Design Pattern concept used here for making listener
        On Every status change -> making the order class know that there is a status change
        Order -> observer
        OrderStatus -> Observable

        Observing the Order Status
        Based on change in status in OrderStatus -> Do something in the Order
        """
        if order_status == self.order_status.PAYMENT_COMPLETE.name:
            # create new delivery for every item of the order
            # for the simplicty of code
            # in reality -> delivery for a order will depend on lot of things
            # that is out of scope of this LLD exercise
            for item in self.item_list:
                # for now keeping quantity as 1 for every item
                # for simplicity
                item_dict = {item:1}
                delivery = Delivery(item_dict, self.order_id)
                self.deliveries.append(delivery)
        
        if order_status == self.order_status.COMPLETED.name:
            # order status is completed
            # generate an invoice
            # for every item seperately for simplicity
            # storing them in an invoices list which can further used
            for item in self.item_list:
                invoice = Invoice(self.order_id, item)
                self.invoices.append(invoice)


class ReturnOrder:
    """
    Return Order is seperate from Order For seperation of concerns
    Return Order and Order are seperate because there are some behaviours which are different
    in both the classes
    So to avoid tight coupling between these two cases -> we have made two seperate classes
    Concept of Order and Return order is different
    Its best to keep both of them seperate
    """

    def __init__(self, items_list, source_add, destination_add):
        self.order_details = OrderDetails(source_add, destination_add)
        self.items_list = items_list
        self.amount_refunded = self.calc_amount_refunded()
    
    def calc_amount_refunded():
        total_amount = 0
        for item in self.items_list:
            total_amount = total_amount + item.get_price()
        
        return total_amount



"""
Note: It’s important to note that calling an enumeration with a member’s value as an argument can make you 
feel like you’re instantiating the enumeration. However, enumerations can’t be instantiated, as you already know
"""

"""
Accessing Enum
class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

Semaphore.RED.name -> 'RED'
Semaphore.RED.value -> 1
"""


class OrderStatus(Enum):
    """
    Enum of Order Status
    """
    CHECKOUT, PAYMENT, PAYMENT_COMPLETE, IN_FLIGHT, COMPLETED = 1, 2, 3, 4, 5


class Delivery:
    """
    Class for Delivery
    """
    def __init__(self, item_dict, order_details):
        self.delivery_id = uuid.uuid4()
        self.item_dict = item_dict
        self.status = DeliveryStatus
        self.order_details = order_details

class DeliveryStatus(Enum):
    """
    Enum for delivery status
    """
    UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6


class Payment:
    """
    Class for Payments 
    There can be different Payment Methods which can be used to make payment
    """
    def __init__(self):
        self.payment_id = uuid.uuid4()
        self.payment_method = PaymentMethods
        self.payment_status = PaymentStatus

class PaymentMethods(Enum):
    """
    Enum contaning all the payment methods possible
    """
    UPI, CASH, CC, NETBANKING = 1, 2, 3, 4

class PaymentStatus(Enum):
    """
    Enum containing all the payment status possible
    """
    UNPAID, PENDING, COMPLETED, DECLINED, REFUNDED = 1, 2, 3, 4, 5


class Invoice:
    """
    Class for Creating Invoice -> after Order is complete
    Invoice is generated for every item seperately for simplicity
    """
    def __init__(self, order_id, item):
        self.invoice_id = uuid.uuid4()
        self.order_id = order_id
        self.item = item



class Address:
    """
    Class defining address object
    """
    def __init__(self, street: str, city: str, state: str, zip_code: str, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
    
    def get_address(self):
        """
        Concatenating the parts of address and returning it
        """
        return self.street+" "+self.city+" "+self.state+" "+self.country+" "+self.zip_code


class Customer:
    """
    Customer Class -> Containing all the data members and variable functions
    of the customer class
    """
    cart = Cart()
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    

    def return_order(self, item_list):
        # just created random addresses here for simplicity
        # but for a customer, we can also store list of addresses
        # and pass any address from it
        # for sender address we can keep address of amazon in a constant
        dest_add = Address("abc", "def", "ijk", 123, "india")
        source_add = Address("abc", "def", "ijk", 123, "aus")
        return_order_obj = ReturnOrder(item_list, source_add, dest_add)


    def view_item(self, name: str):
        item = Item(name)
        return item.get_item()

    def buy_item(self, item):
        """
        Convert the single item in an order
        """
        item_list = [item]
        # just created random addresses here for simplicity
        # but for a customer, we can also store list of addresses
        # and pass any address from it
        # for sender address we can keep address of amazon in a constant
        source_add = Address("abc", "def", "ijk", 123, "india")
        dest_add = Address("abc", "def", "ijk", 123, "aus")
        order = Order(item_list, source_add=source_add, destination_add=dest_add)
        return order


    def add_to_cart(self, item):
        """
        add an item to a cart
        """
        cart.add_item(item)

    def view_items_in_cart(self) -> list:
        """
        Giving back the list of items in the cart
        """
        return cart.get_items_list()

    def checkout(self):
        """
        Convert items in the cart in an order
        """
        # convert items of cart into order
        items_list = cart.get_items_list()
        source_add = Address("abc", "def", "ijk", 123, "india")
        dest_add = Address("abc", "def", "ijk", 123, "aus")
        order = Order(items_list, source_add=source_add, destination_add=dest_add)
        return order


class Product:
    """
    Class Defining a Product.
    Ex -> Earphone is a product. Lot of items can be an earphone
    """
    def __init__(self, name: str):
        self.product_id = uuid.uuid4()
        self.name = name

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
    
    cart = Cart()
