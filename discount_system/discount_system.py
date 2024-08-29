
from time import time
from abc import ABC, abstractmethod
from enum import Enum




class ProductModel:
    product_list = []
    def __init__(self, name, price):
        self.id = time.time()
        self.name = name
        self.price = price

    @classmethod
    # only do this if interviewer tells to demo
    # some features and time is left
    def add_product_to_list(cls, product_obj):
        cls.product_list.append(product_obj)


# Decorator pattern used here
# to apply discounts on products of shopping cart

# first in shopping cart -> products are filled
# then discounts are applied

# here discount will be the amount of discount
# from different discount strategies applied on the cart products
class ShoppingCartModel:

    def __init__(self, product_list, discount_list):
        self.products = []
        self.discount_amount_list = []


    def add_product_in_cart(self, product_obj):
        self.products.append(product_obj)

    
    def add_discount_on_cart(self, discount_amount):
        self.discount_amount_list(discount)
    

     def calculate_total(self):
        total = sum(product.price for product in self.products)
        total_discount = sum(discount.apply_discount(self) for discount in self.discounts)
        return total - total_discount



class UserType(Enum):
    ADMIN = 1
    CUSTOMER = 2


class UserModel:
    def __init__(self, name, user_type):
        self.id = time.time()
        self.name = name
        self.user_type = user_type


class CustomerSubscriptionModel:
    def __init__(self, user):
        self.user = user
        self.points = 0

    
    def add_points_to_user(self, point):
        # only if user type is customer for self.user
        # points are added
        self.points = self.points + point


class IDiscountStrategy(ABC):
    def __init__(self):
        pass
    
    def apply_discount(self, cart):
        pass



class ProductBasedDiscount(IDiscountStrategy):
    product_discount_list = []
    def __init__(self, product_name: str, discount_amount: float):
        self.product_name = product_name
        self.discount_amount = discount_amount
    
    def product_discount_list(cls, product_discount_obj):
        cls.product_discount_list.append()

    def apply_discount(self, cart):
        # access class variable in instance method
        # MyClass.class_variable += 1

        discount = 0
        for product in cart.products:
            if product.name == self.product_name:
                discount += self.discount_amount
        return discount 


class PercentageDiscount(IDiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, cart: ShoppingCart) -> float:
        total = sum(product.price for product in cart.products)
        return total * (self.percentage / 100.0)

class DayBasedDiscount(IDiscountStrategy):
    day_discount_list = []


    def __init__(self, discount_amount: float, day):
        self.discount_amount = discount_amount
        self.day = day

    def add_day_discount_to_list(cls, day_discount_obj):
        cls.day_discount_list.append(day_discount_obj)

    def apply_discount(self, cart, day_enum) -> float:
        
       for daydiscount_obk in DayBasedDiscount.discount_list:
        if daydiscount_obj.day == day_enum:
            return daydiscount_obj.amount

# make class for subscription based
# it will tale customer subscription 
# and apply points based on that



"""
services
"""

class ProductService:
    def __init__(self):
        pass
    

    def add_product(self):
        pass


class CustomerService:
    def __init__(self):
        pass
    

    def add_customer(self, name):
        pass
    
    def add_product_in_cart(self, product, cart):
        pass


class AdminService:
    def __init__(self):
        pass
    
    def add_admin(self, name):
        pass

    def add_discount_strategy(self, discount_strategy_name):
        pass


class DiscountService:
    def __init__(self):
        # obj of discount strategy appended here
        self.discount_strategies = []
    
    # this will be called from inside admin service only
    # only admin can add discount strategy -> validation will be 
    # put here
    def add_new_discount_strategy(self, user, discount_strategy_name, rule_set):
        pass
    
    def apply_discount_to_shopping_cart(self, cart, discount_strategy_list=[]):
        # discount_strategy_list -> optional parameter
        # based on discount strategy -> apply discount on the cart

        # return the discount amounted of the cart