"""
Models
"""

from enum import Enum
import time
from abc import ABC, abstractmethod



class UserType(Enum):
    BROKER = 1
    BUYER = 2


class UserModel:
    """
    User Model
    User Model will have only user attributes
    """

    total_user = []

    def __init__(self, name, user_type: UserType):
        self.id = time.time()  # timestamp as the unique user id
        self.name = name
        self.user_type = user_type
        # self.property_list = []  # type ProperyModel

    # def add_prop_to_user(self, prop_obj):
    #     """
    #     add prop to curr user
    #     Append in the list
    #     """
    #     self.property_list.append(prop_obj)

    @staticmethod
    def add_user_to_total_list(user_obj):
        UserModel.total_user.append(user_obj)


class PropertyModel:
    """
    Property Model
    """

    prop_counter = 0
    total_prop = []

    def __init__(self, city: str, price: int, size: str):
        self.id = PropertyModel.prop_counter + 1
        # increment the class variable also
        PropertyModel.prop_counter = PropertyModel.prop_counter + 1
        self.city = city
        self.price = price
        self.size = size
        self.sold = False

    def sell_curr_prop(self):
        """ """
        self.sold = True

    @staticmethod
    def add_prop_to_total_list(prop_obj):
        """
        add curr property to list of total properties
        """
        PropertyModel.total_prop.append(prop_obj)


class UserPropModel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_curr_prop_to_total_list():
        pass


class BrokerPropModel(UserPropModel):
    """
    So we will not store property at the user level
    We will store User<>Property relationship in a seperate model
    This Model will have two instance vars
    User
    Property
    One user can have multiple property
    Store a list at the class level having all the
    BrokerPropModel

    -> Only the properties which has not been sold till now
    are active

    If need to fetch list of property for user
    Scan the list and find all the property of a broker

    If need to find a property attached to which user
    again scan the list and find a property attached to which user

    This is how it will be implemented
    """

    brok_prop_total_list = []

    def __init__(self, user: UserModel, prop: PropertyModel):
        self.id = time.time()
        self.user = user
        self.property = prop

    @staticmethod
    def add_curr_prop_to_total_list(prop_obj):
        BrokerPropModel.brok_prop_total_list.append(prop_obj)


class BuyerPropModel(UserPropModel):
    """
    Buyer <> Prop Relationship Model
    Similar lines to Broker<>Prop Relationship
    """

    buyer_prop_total_list = []

    def __init__(self, user: UserModel, prop: PropertyModel):
        self.id = time.time()
        self.user = user
        self.property = prop

    @staticmethod
    def add_curr_prop_to_total_list(prop_obj):
        BuyerPropModel.buyer_prop_total_list.append(prop_obj)


class TransactionsModel:
    """
    Will store all the transactions of buy and sell of property
    this model will give which broker sold to which buyer

    """

    all_transactions_list = []

    def __init__(self, buyer: UserModel, broker: UserModel, prop: PropertyModel):
        self.id = id
        self.buyer = buyer
        self.broker = broker
        self.property = prop

    @staticmethod
    def add_curr_transac_to_total_list(transac_obj):
        TransactionsModel.all_transactions_list.append(transac_obj)


"""
Services
"""


class UserService:
    def __init__(self):
        pass

    def add_user(self, name: str, user_type: UserType):
        """
        Functional API to add User
        Responsibility
        -> Do all the validation
        -> Have some wrapper logic
        Before adding User to the DB (UserModel)
        """

        if not isinstance(name, str):
            raise Exception("user_name should be string")

        if user_type not in UserType:
            # can be extended to print valid enums
            raise Exception(f"user_type {user_type} should be valid UserType")

        user_model_obj = UserModel(name, user_type)
        UserModel.add_user_to_total_list(user_model_obj)

        return user_model_obj

    
    def list_my_property(self, user_name: str):
        """
        Functional API to list my property
        Responsibility
        -> Do all the validation
        -> Fetch user for user_name
        -> check if user is a broker or not
        -> if user is a broker then only list its property
        """

        total_prop_list = []
        for broker_prop in BrokerPropModel.brok_prop_total_list:
            if user_name == broker_prop.user.name:
                total_prop_list.append(broker_prop.property)

        
        # if the list is empty -> means user is registered as buyer
        if len(total_prop_list) > 0:
            return total_prop_list
        else:
            raise Exception(f"User {user_name} is listed as a buyer")


class PropertyService:
    def __init__(self):
        pass

    def add_property(self, city: str, price: int, size: str, user: UserModel):
        """
        Functional API to add Propery
        Responsibility
        -> Do all the validation
        -> Check that property is added by broker only
        -> Have some wrapper logic
        Before adding propery to the DB (PropertyModel)
        """
        if not isinstance(city, str):
            raise Exception("city should be string")

        if not isinstance(price, int):
            raise Exception("price should be int")

        if not isinstance(size, str):
            raise Exception("size should be str")

        property_obj = PropertyModel(city, price, size)
        # user.add_prop_to_user(property_obj)

        # property will be added by the broker
        broker_prop_obj = BrokerPropModel(user, property_obj)

        # add the broker prop relationship into total list
        BrokerPropModel.add_curr_prop_to_total_list(broker_prop_obj)

        # add prop object into total list
        PropertyModel.add_prop_to_total_list(property_obj)

        return property_obj

    def search_propery(self, user: UserModel, city: str, price_range: tuple):
        """
        Functional API to search Property
        Responsibility
        -> Do all the validation
        -> list the property which is not sold
        -> Additionally filter the property which matches city, price_range
        -> At last return the suitable buyer_property relationship object
        """

        if not isinstance(city, str):
            raise Exception("city should be string")

        if not isinstance(price_range, tuple):
            raise Exception("price_range should be tuple of min & max price")

        total_available_prop_list = []

        for broker_prop in BrokerPropModel.brok_prop_total_list:
            if not broker_prop.property.sold:
                total_available_prop_list.append(broker_prop)

        suitable_prop = []

        for broker_prop in total_available_prop_list:
            if (
                broker_prop.property.price >= price_range[0]
                and broker_prop.property.price <= price_range[1]
                and broker_prop.property.city == city
            ):
                suitable_prop.append(broker_prop)

        
        return suitable_prop
        
        


class TransactionService:
    def __init__(self):
        pass
    
    def buy_property(self, user:UserModel, prop_id: int):
        """
        Functional API to buy Property
        Responsibility
        -> Do all the validation
        -> check if the property is sold or not if sold print error message
        -> if property is not sold -> sell it to the current user
        """
        if not isinstance(prop_id, int):
            raise Exception("property ID should be int")
        

        for broker_prop in BrokerPropModel.brok_prop_total_list:
            if broker_prop.property.id  == prop_id:
                if broker_prop.property.sold:
                    print(f"Property with {broker_prop.property.id} already sold")
                else:
                    # set property to sold
                    broker_prop.property.sold = True
                    # initialise a buyer_prop_obj
                    buyer_prop_obj = BuyerPropModel(user, broker_prop.property)

                    # add buyer_prop_obj to total list
                    BuyerPropModel.add_curr_prop_to_total_list(buyer_prop_obj)

                    # add into transaction service 
                    transac_obj = TransactionsModel(user, broker_prop.user, broker_prop.property)
                    TransactionsModel.add_curr_transac_to_total_list(transac_obj)

                    print(f"property {prop_id} sold to {user.name}")
            

"""
Api Handler
Controller class -> Redirects to specific service

"""


class ApiHandler:
    def __init__(self):
        pass

    def add_user(self, name: str, user_type: UserType):
        user_service = UserService()
        user_obj = user_service.add_user(name, user_type)
        return user_obj

    def add_property(self, city: str, price: int, size: str, user: UserModel):
        prop_service = PropertyService()
        prop_model = prop_service.add_property(city, price, size, user)
        return prop_model

    def search_propery(self, user, city, price_range):
        prop_service = PropertyService()
        suitable_prop = prop_service.search_propery(user, city, price_range)
        return suitable_prop

    def buy_property(self, user, prop_id):
        transac_service = TransactionService()
        transac_service.buy_property(user, prop_id)
    
    def list_my_property(self, user_name):
        user_service = UserService()
        prop_obj_list = user_service.list_my_property(user_name)
        return prop_obj_list


def main():
    api_handler = ApiHandler()

    print("Add 1st broker")
    broker1_obj = api_handler.add_user("mayank", UserType.BROKER)
    print(broker1_obj.name)

    print("\n")

    print("Add 2nd broker")
    broker2_obj = api_handler.add_user("Mohit", UserType.BROKER)
    print(broker2_obj.name)

    print("\n")

    print("Add 1st buyer")
    buyer1_obj = api_handler.add_user("saurabh", UserType.BUYER)
    print(buyer1_obj.name)

    print("Add 2nd buyer")
    buyer2_obj = api_handler.add_user("anand", UserType.BUYER)
    print(buyer2_obj.name)

    print("\n")
    print("Add 1st property")
    prop1_obj = api_handler.add_property("Banglore", 1000, "1-BHK", broker1_obj)
    print(prop1_obj.id)

    print("\n")
    print("Add 2nd property")
    prop2_obj = api_handler.add_property("Banglore", 2000, "2-BHK", broker1_obj)
    print(prop2_obj.id)

    print("\n")
    print("Add 3rd property")
    prop3_obj = api_handler.add_property("Pune", 1500, "2-BHK", broker2_obj)
    print(prop3_obj.id)

    print("\n")
    print("Add 4th property")
    prop3_obj = api_handler.add_property("Banglore", 1500, "2-BHK", broker2_obj)
    print(prop3_obj.id)

    print("\n")
    # Case 1 -> user 1 searches property
    print(f"Search the property for buyer: {buyer1_obj.name}")
    suitable_prop = api_handler.search_propery(buyer1_obj, "Banglore", (1000, 2000))
    
    res_prop_dict_tuple = {}

    for broker_prop in suitable_prop:
        res_prop_dict_tuple[broker_prop.property.id] = (
            broker_prop.user.name,
            broker_prop.property.city,
            broker_prop.property.price,
            broker_prop.property.size,
        )

    print(res_prop_dict_tuple)



    # Case 2 -> buyer 1 buys the property 1
    print("\n")
    prop_id = 1
    api_handler.buy_property(buyer1_obj, prop_id)

    # Case 3 -> buyer 2 buys the property 1
    print("\n")
    prop_id = 1
    api_handler.buy_property(buyer2_obj, prop_id)

    # Case 4 -> buyer 3 buys property 2
    print("\n")
    prop_id = 4
    api_handler.buy_property(buyer2_obj, prop_id)

    # Case 5 -> listmypropery -> buyer -> will give error
    print("\n")
    print(f"property list of User {broker1_obj.name}")
    prop_obj_list = api_handler.list_my_property(broker1_obj.name)
    for prop in prop_obj_list:
        print(f"{prop.id} and its sold_status: {prop.sold}")
    
    # Case 6 -> listmypropery -> buyer -> will give error
    print("\n")
    prop_obj_list = api_handler.list_my_property(buyer2_obj.name)


if __name__ == "__main__":
    main()
