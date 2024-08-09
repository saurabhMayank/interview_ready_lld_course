from time import time

class UserModel:
    def __init__(self, name: str, email: str):
        self.id = time.time() # unique id
        self.name = name
        self.email = email


class GroupModel:
    def __init__(self, name: str, user_list):
        self.id = time.time()
        self.name = name
        self.user_list = user_list


class ExpenseModel:
    def __init__(self, title, amount, paidBy, group_obj):
        self.id = time.time()
        self.title = title
        self.amount = amount
        self.paidBy = paidBy
        self.group = group_obj


class SplitModel:
    def __init__(self, user, amount):
        self.id = time.time()
        self.user = user
        self.amount = amount


class SplitType(Enum):
    EXACT = 1
    PERCENTAGE = 2 
    EQUAL = 3


class UserBalance:
    def __init__(self, user,  grp_obj):
        self.user = user
        self.grp = grp_obj
        self.user_bal_dict = {}

    
    def update_user_bal(self, grp_user, amount):
        user_bal_dict[grp_user] = amount


class BalanceSheet:
    def __init__(self, group, creditUser, total_amount, amount_split_mp ):
        self.group = group
        self.creditUser = creditUser
        self.total_amount = total_amount
        self.amount_split_mp = amount_split_mp



"""
Services
"""

class UserService:
    def __init__(self):
        pass

    def add_user(self, name, email):
        pass
    


class GroupService:
    def __init__(self):
        pass
    
    def create_group(self, name):
        pass
    
    def add_users_to_group(self, user_obj):
        pass

    
    def update_group(self, group_obj, name, user_obj_list):
        pass


class ExpenseService:
    def __init__(self):
        pass


    def create_expense(self):
        pass
    
    def split_expense(self):
        pass
    
    def 


class SplitService:
    def __in

    