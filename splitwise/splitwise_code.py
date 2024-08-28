# saving all the data in memory class variable

from time import time
from abc import ABC, abstractmethod

class UserModel:
    # class variable -> access via class name
    user_list = []
    def __init__(self, name: str, email: str):
        self.id = time.time() # unique id
        self.name = name
        self.email = email

    @classmethod
    def add_user_to_list(cls, user_obj):
        cls.user_list.append(user_obj)


class GroupModel:
    group_list = []
    def __init__(self, name: str):
        self.id = time.time()
        self.name = name
        self.created_at = time.time()
    
    @classmethod
    def add_group_to_list(cls, group_obj):
        cls.group_list.append(group_obj)
    
    @classmethod
    def update_group_obj(cls, group_obj, name):
        for grp in cls.group_list:
            if grp.id == group_obj.id:
                grp.name = name

    

class UserGroupModel:
    user_group_list = []
    def __init__(self, user, group):
        self.id = time.time()
        self.user = user
        self.group = group
    
    @classmethod
    def add_user_group_to_list(cls, user_group_obj):
        cls.user_group_list.append(user_group_obj)


class ExpenseModel:
    exp_obj_list = []
    def __init__(self, title, amount, paidBy, group_obj):
        self.id = time.time()
        self.title = title
        self.amount = amount
        self.group = group_obj
        self.is_settled = False

    @classmethod
    def add_expense_to_list(cls, exp_obj):
        cls.exp_obj_list.append(exp_obj)
    
    @classmethod
    def settle_expense(cls, exp_obj):
        # find that data in the list
        # and mark it settled
        for exp in cls.exp_obj_list:
            if exp_obj.id == exp.id:
                exp.is_settled = True


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
    user_balance_list = []
    def __init__(self, user,  grp_obj):
        self.id = time.time()
        self.user = user
        self.grp = grp_obj
        self.user_bal_dict = {}

    @classmethod
    def update_grp_user_bal(cls, user_bal_obj, grp_user, amount):
        for user_bal in cls.user_balance_list:
            if user_bal_obj.id == user_bal:
                user_bal.user_bal_dict[grp_user] = amount
    
    @classmethod
    def get_user_balance(cls, user, group):
        for user_bal in user_balance_list:
            if user_bal.user.id == user.id and user_bal.group.id == group.id:
                return user_bal 
    
    @classmethod
    def add_user_balance_to_list(cls, user_bal_obj):
        cls.user_balance_list.append(user_bal_obj)



class BalanceSheet:
    balance_sheet_list = []
    def __init__(self, creditUser, exp_obj, amount_split_mp):
        self.id = time.time()
        self.creditUser = creditUser
        self.exp = exp_obj
        self.amount_split_mp = amount_split_mp
    
    @classmethod
    def add_balance_sheet_to_list(cls, balance_sheet_obj):
        cls.balance_sheet_list.append(balance_sheet_obj)



"""
Services
"""

class UserService:
    def __init__(self):
        pass

    def add_user(self, name, email):
        user_obj = UserModel(name, email)
        UserModel.add_user_to_list(user_obj)
    


class GroupService:
    def __init__(self):
        pass
    
    def create_group(self, name):
        group_obj = GroupModel(name)
        GroupModel.add_group_to_list(group_obj)

    def update_group(self, group_obj, name):
        GroupModel.update_group_obj(group_obj, name)
    
    def add_users_to_group(self, user_obj, group_obj):
        user_group_obj = UserGroupModel(user_obj, group_obj)
        UserGroupModel.add_user_group_to_list(user_group_obj)

    
    


class ExpenseService:
    def __init__(self):
        pass


    def create_expense(self, name, paidBy, amount, grp):
        exp_obj = ExpenseModel()
    
    def split_expense(self):
        pass
    
    def settle_expense(self):
        pass

class SplitService:
    def __init__(self):
        pass
    

    def split_factory(user, split_type, exp_obj, percentage_mp={}, exact_amount={}):
        pass


class ISplitFactory(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def create_split(self):
        pass
    

class ExactSplitFactory(ISplitFactory):
    def __init__(self):
        pass
    

    def create_split(self, exp, payingUser, exact_mp):
        pass


class EqualSplitFactory(ISplitFactory):
    def __init__(self):
        pass
    

    def create_split(self, exp, payingUser):
        pass


class PercentageSplitFactory(ISplitFactory):
    def __init__(self):
        pass
    

    def create_split(self, exp, payingUser, percentage_mp):
        pass



class TransactionService:
    def __init__(self):
        pass
    
    def update_balance_sheet(self, payingUser, exp_obj, split_list):
        user_split_mp = {}

        for split in split_list:
            user_split_mp[split.user] = split.amount

        balance_sheet_obj = BalanceSheet(payingUser, exp_obj, user_split_mp)
        BalanceSheet.add_balance_sheet_to_list(balance_sheet_obj)
    
    def show_user_balance(self, user, group):
        user_bal = UserBalance.get_user_balance(user, group)
        return user_bal
    
    def add_user_balance(self, user, group, user_amount_mp):
        user_bal = UserBalance(user, group, user_amount_mp)
        UserBalance.add_user_balance_to_list(user_bal)
    

    def update_user_balance(self, user_bal_obj, grp_user, amount):
        UserBalance.update_grp_user_bal(user_bal_obj, grp_user, amount)


class ApiHandler:
    def __init__(self):
        pass

    # this will contain all the functions
    # main will call the api handler
    # api handler will call the specific classes


def main():
    api_handler = ApiHandler()
    # main will contain the script for running the code


if __name__ == "__main__":
  main()