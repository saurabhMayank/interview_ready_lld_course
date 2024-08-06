
import time
from datetime import datetime, timedelta


"""
Models
"""

class ProductModel:
    def __init__(self, name: str, price: int):
        self.id = time.time() # unique id
        self.name = name
        self.price = price
    



class DealsModel:
    # containing all the deals created till now

    # time_limit -> will always be in seconds -> for demo purpose


    total_deals_list = []
    def __init__(self, name, prod_obj, item_count, time_limit, start_time):
        self.id = time.time() # unique id
        self.name = name
        self.prod_obj = prod_obj
        self.item_count = item_count
        self.time_limit = time_limit
        self.start_time = start_time
        self.deal_active = True # initially deal is active when created
    

    def update_time(self, new_time_limit):
        """
        """
        self.time_limit = new_time_limit

    
    def update_item_count(self, new_item_count):
        """
        """
        self.item_count = new_item_count
    

    def make_deal_inactive(self):
        """
        """
        self.deal_active = False
    

    def add_deal_to_total(deals_obj):
        """
        """
        DealsModel.total_deals_list.append(deals_obj)


class UserModel:
    def __init__(self, name: str, email: str):
        self.id = time.time()
        self.name = name
        self.email = email


class UserDealTransactionModel:
    """
    This Model will store data of which user has claimed which deal
    """
    total_userDeal_list = []

    def __init__(self, user_obj, deal_obj):
        self.id = time.time()
        self.user = user_obj
        self.deal = deal_obj
    

    def add_userDeal_to_total_list(user_deal_obj):
        UserDealTransactionModel.total_userDeal_list.append(user_deal_obj)


"""
Services
"""


class ProductService:
    def __init__(self):
        pass
    

    def add_product(self, name: str, price: int):
        """
        """
        prod_obj = ProductModel(name, price)
        return prod_obj




class UserService:
    def __init__(self):
        pass
    

    def add_user(self, name: str, email: str):
        """
        """
        if not isinstance(name, str):
            raise Exception("name should be str")
        
        if not isinstance(email, str):
            raise Exception("email should be str")

        
        user_obj = UserModel(name, email)

        return user_obj


class DealService:
    def __init__(self):
        pass
    

    def create_deal(self,name, prod_obj, item_count, time_limit, start_time):
        """
        """
        if not isinstance(item_count, int):
            raise Exception("item_count should be int")
        
        if not isinstance(time_limit, int):
            raise Exception("time_limit should be int")

        # validation on start_time

        deals_obj = DealsModel(name, prod_obj, item_count, time_limit, start_time)
        DealsModel.add_deal_to_total(deals_obj)

        return deals_obj
    

    def update_deal(self, deals_obj, item_count=-1, time_limit=-1):
        """
        Update possible for attributes
        i) Item count
        ii) time_limit -> seconds

        Update also add_deal_to_total to total list

        Constraint:
            -> once the deal has been claimed by any user
            -> The deal object cannot be updated
            -> Till the deal has not been claimed
            -> Till then only it can be updated

        """

        if item_count != -1 and isinstance(item_count, int):
            deals_obj.update_item_count(item_count)
        
        if time_limit != -1 and isinstance(time_limit, int):
            deals_obj.update_time(time_limit)


        # extension
        for curr_deal_obj in DealsModel.total_deals_list:
            if curr_deal_obj.name == deals_obj.name:
                if item_count != -1 and isinstance(item_count, int):
                    curr_deal_obj.update_item_count(item_count)
                    
                if time_limit != -1 and isinstance(time_limit, int):
                    curr_deal_obj.update_time(time_limit)
                    
            break
        
        return deals_obj
    

    def end_deal(self, deals_obj):
        """
        Make deal inactive
        -> Make deal inactive from deal_obj and UserDealTransactionModel

        Constraints on Deal Ending
            -> Deal can be ended if either user has claimed or not claimed
            the deal

            -> Also this data needs be updated in the UserDealModel object

        """
        
        for curr_deal_obj in DealsModel.total_deals_list:
            if curr_deal_obj.name == deals_obj.name:
                deals_obj.make_deal_inactive()
                curr_deal_obj.make_deal_inactive()
            break



        for user_deal_obj in UserDealTransactionModel.total_userDeal_list:
            if user_deal_obj.name == user_deal_obj.name:
                user_deal_obj.deal.make_deal_inactive()

        print(f"{deals_obj.name} has ended")


class UserDealTransactionService:
    """
    """
    def __init__(self):
        pass

    
    def claim_deal(self, user_obj, deal_obj):
        """
        Update Item count in deals obj and UserDealModel obj
        """

        if not deal_obj.deal_active:
            raise Exception("Deal has ended")

        if deal_obj.item_count == 0:
            raise Exception("Deal has no item count left of product")

        # if deal time has ended or not
        curr_time = datetime.now()

        deal_time_limit = deal_obj.start_time + timedelta(seconds=deal_obj.time_limit)

        if curr_time > deal_time_limit:
            raise Exception("Deal time is already over")

        
        for user_deal_obj in UserDealTransactionModel.total_userDeal_list:
            if user_deal_obj.deal.name == deal_obj.name and user_deal_obj.user.name == user_obj.name:
                raise Exception(f"User {user_obj.name} has already claimed deal {deal_obj.name}")
    

        # claim the deal

        # update in UserDeal Transaction

        deal_obj.update_item_count(deal_obj.item_count-1)
        user_deal_model_obj = UserDealTransactionModel(user_obj, deal_obj)
        UserDealTransactionModel.add_userDeal_to_total_list(user_deal_model_obj)

        # reduce the item count
        # updated in total deals list
        for curr_deal_obj in DealsModel.total_deals_list:
            if curr_deal_obj.name == deal_obj.name:
                curr_deal_obj.update_item_count(deal_obj.item_count-1)
            break
        
        print(f"Deal is claimed User: {user_obj.name}, deal: {deal_obj.name}")


        
"""
Api Handler
"""
class ApiHandler():
    def __init__(self):
        pass

    
    def add_user(self, name, email):
        user_service_obj = UserService()
        user_obj = user_service_obj.add_user(name, email)
        return user_obj

    def add_product(self, name, price):
        prod_service_obj = ProductService()
        prod_obj = prod_service_obj.add_product(name, price)
        return prod_obj

    
    def create_deal(self, name, prod_obj, item_count, time_limit, start_time):
        deals_service_obj = DealService()
        deals_obj = deals_service_obj.create_deal(name, prod_obj, item_count, time_limit, start_time)
        return deals_obj

    
    def update_deal(self, deals_obj, item_count=-1, time_limit=-1):
        deals_service_obj = DealService()
        deals_obj = deals_service_obj.update_deal(deals_obj, item_count, time_limit)
        return deals_obj

    
    def claim_deal(self, user_obj, deals_obj):
        user_deal_service_obj = UserDealTransactionService()
        user_deal_service_obj.claim_deal(user_obj, deals_obj)
         

    
    def end_deal(self, deals_obj):
        deals_service_obj = DealService()
        deals_service_obj.end_deal(deals_obj)


"""
Main
"""

def main():
    """
    """
    api_handler = ApiHandler()

    # product 1
    prod1_obj = api_handler.add_product("phone", 1000)
    print("--printing product")
    print(prod1_obj.name)
    print(prod1_obj.price)

    # create deal
    start_time = datetime.now()

    # timeLimit -> in seconds
    time_limit = 10
    deal_name = "first_deal"
    item_count = 4
    deals1_obj = api_handler.create_deal(deal_name, prod1_obj, item_count, time_limit, start_time)

    print("---1st deal created---")
    print(f"{deals1_obj.name}, {deals1_obj.prod_obj.name}, {deals1_obj.item_count} ")

    # update deal
    item_count = 3
    time_limit = 7

    deals1_obj = api_handler.update_deal(deals1_obj, item_count, time_limit)

    print("---1st deal updated---")
    print(f"{deals1_obj.name}, {deals1_obj.prod_obj.name}, {deals1_obj.item_count}, {deals1_obj.time_limit} ")


    # create user -> 2 users
    print("\n")
    print("----added users---")

    print("--user 1----")
    user1_obj = api_handler.add_user("mayank", "mayank@abc.com")
    print(user1_obj.name)
    
    print("--user 2----")
    user2_obj = api_handler.add_user("saurabh", "saurabh@abc.com")
    print(user2_obj.name)

    # claim deal

    # case 1 -> user1 has claimed deal1
    print("\n")
    print("---user 1 is claiming deal 1-----")

    api_handler.claim_deal(user1_obj, deals1_obj)

    # case 2 -> user1 trying to claim deal1 again

    # please comment this case and then check next case

    # print("\n")
    # print("---user 1 is claiming deal 1 again-----")

    # working -> it will raise an exception
    # api_handler.claim_deal(user1_obj, deals1_obj)

    # case 3 -> user2 is trying to claim the deal1 but deal time over
    # its in seconds
    # its working -> user2 time will not able to claim the deal
    # as deals1_obj is less than 50 seconds

    # please comment this case to check the next case

    # time.sleep(50)
    # api_handler.claim_deal(user2_obj, deals1_obj)


    # case 4 -> user2 is trying to claim the deal1 within time
    # and count of product is there
    # it is working 

    print("\n")
    api_handler.claim_deal(user2_obj, deals1_obj)

    # case 5 -> user3 is trying to claim deal1 within time and count is there
    print("\n")

    user3_obj = api_handler.add_user("mohit", "mohit@abc.com")
    print(user3_obj.name)

    print("\n")
    api_handler.claim_deal(user3_obj, deals1_obj)



if __name__ == "__main__":
  main()



