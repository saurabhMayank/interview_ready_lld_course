import time
from abc import ABC

class PaymentGateway:
    # Main class of the system
    def __init__():
        pass


class User:
    """
    User class -> User can create transaction
    """
    def __init__(self, name:str, email: str):
        self.name = name
        self.email = email
        self.id = time.time()
    
    def create(self, t:Transaction):
        pass


class Transaction:
    """
    Transaction Class -> Attributes of a transaction
    """
    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def change_state(self):
        pass


class TransactionStatus(ABC):
    """
    Transaction Status Class -> Possible states of a transaction
    Abstract transaction class -> All the transaction status class will inherit this
    """
    def __init__(self):
        pass

class PendingTransactionStatus(TransactionStatus):
    """
    Pending State of a transaction
    """
    pass


class SuccessTransactionStatus(TransactionStatus):
    """
    Success State of a transaction
    """
    pass


class CancelledTransactionStatus(TransactionStatus):
    """
    Cancelled State of a transaction
    """
    pass



class RuleEngine():
    """
    Rule Engine for all types of Validation
    -> Validate Transaction
    -> Detect Fraud
    """
    def __init__(self):
        pass

    def validate_transaction(self, t:Transaction):
        """
        validate transaction to be valid or not based on the rules
        """
        pass

    def detect_fraud(self, t:Transaction):
        """
        detect if transaction is fraudlent or not
        """
        pass





class Bank:
    """
    Class Representing attributes of a bank
    """
    def __init__(self, name: str, address: Address, ifsc: int):
        self.id = time.time() # unique id current timestamp
        self.name = name
        self.address = address
        self.ifsc = ifsc


    def start(self, t: Transaction):
        pass

    def poll(self, t: Transaction):
        pass


    def observe(self, t: Transaction):
        pass


class Address:
    """
    Address class
    """
    pass

