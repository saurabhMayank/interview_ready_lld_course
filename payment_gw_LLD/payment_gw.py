import time
from abc import ABC
from enum import Enum


class PaymentGateway:
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
    def __init__(self, amount: Amount, status: TransactionStatus, sender_acc: Account, 
                 reciever_acc: Account, description: str, payment_method: PaymentMethod):
        self.amount = amount
        self.status = status
        self.sender_acc = sender_acc   # who is sending the money
        self.reciever_acc = reciever_acc  # who is recieving the money
        self.description = description
        self.payment_method = payment_method # how is sender sending money to reciever


    def change_state(self, new_status: TransactionStatus):
        """
        Change of State of this State Machine
        On every change of state -> need to send some kind of notification
        Informing other entities -> who are observing or polling for this state
        """
        self.status = new_status
        # whenever new state of transaction is set -> notify the involved entities
        # about the state of transaction -> that is the sender and reciever accounts
        self.status.notify_status(self.sender_acc, self.reciever_acc)



class Amount:
    """
    Amount class having amount value and currency
    """
    def __init__(self, amount_val: float, currency: Currency);
        self.amount_val = amount_val
        self.currency = currency


class PaymentMethod(Enum):
    card = 1
    bank_transfer = 2 # internet banking
    upi = 3


class Currency(Enum):
    """
    Limited set of currencies possible
    """
    inr = 1
    usd = 2
    pound = 3
    diram = 4



class TransactionStatus(ABC):
    """
    Transaction Status Class -> Possible states of a transaction
    Abstract transaction class -> All the transaction status class will inherit this
    """
    def __init__(self):
        pass
    
    @abstractmethod
    def notify_status(self, sender_acc:Account, reciever_acc:Account):
        """
        Observer Pattern Use :-
        Account class is observing the Transaction Status Class
        Whenever there is a change in status -> Account class needs to be notified about it
        """
        pass

class PendingTransactionStatus(TransactionStatus):
    """
    Pending State of a transaction
    """
    def __init__(self):
        pass


    def notify_status(self, sender_acc:Account, reciever_acc:Account):
        """
        sending pending state notification to both sender and reciever
        Informing that the payment is in process
        """
        pass


class SuccessTransactionStatus(TransactionStatus):
    """
    Success State of a transaction
    """
    def __init__(self):
        pass


    def notify_status(self, sender_acc:Account, reciever_acc:Account):
        """
        sending success state notification to both sender and reciever
        Informing that the payment is in process
        """
        pass


class CancelledTransactionStatus(TransactionStatus):
    """
    Cancelled State of a transaction
    """
    def __init__(self):
        pass


    def notify_status(self, sender_acc:Account, reciever_acc:Account):
        """
        sending cancelled state notification to both sender and reciever
        Informing that the payment is in process
        """
        pass


class RuleEngine():
    """
    Rule Engine for all types of Validation
    -> Validate Transaction
    -> Detect Fraud
    """
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def validate_transaction(self, t:Transaction):
        """
        validate transaction to be valid or not based on the rules
        Based on type of transaction -> we can have a different ways to validate a transaction
        Here we can use strategy pattern -> to have different strategies for validating different transactions

        There can be different strategies -> which have their own validate method -> to validate the class
        """
        self.strategy.validate(t) # every strategy has validate function to validate a transaction
        # user can choose -> which strategy to use based on requirements of the system

    def detect_fraud(self, t:Transaction):
        """
        detect if transaction is fraudlent or not
        """
        pass


class Strategy(ABC):
    """
    Abstract class strategy for validating a transaction
    which will be implemented by different strategies

    There can be different strategies for validating a function. Not going into that right now
    """
    def __init__(self):
        pass

    def validate(self, t:Transaction):
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


class Account:
    """
    Every account is part of a bank
    Association relationship with the bank
    Every bank has multiple accounts
    """
    def __init__(user:User, bank:Bank):
        self.user = user
        self.bank = bank
        self.id = time.time() # unique id for an account



class main:
    """
    Main class of the system
    """
    user = User("Mayank", "mayank@xyz.com")
    reciever = User("Gaurav", "gaurav@xyz.com")
    status = PendingTransactionStatus()
    currency = Currency()
    amount = Amount(9024403.00, currency.inr)
    address = Address()
    bank = Bank("hdfc",address, 89340322)
    bank_2 = Bank("kotak", address, 2343222332)
    sender_acc = Account(user, bank)
    reciever_acc = Account(reciever, bank_2)


    payment_method = PaymentMethod()
    t = Transaction(amount, status, sender_acc, reciever_acc, "test", payment_method.card)
    user.create(t)

    strategy = Strategy()
    rule_engine = RuleEngine(strategy)

    rule_engine.validate_transaction(t)

    new_status = SuccessTransactionStatus()

    t.change_state(new_status)