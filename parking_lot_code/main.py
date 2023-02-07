from enum import Enum
class VehicleType(Enum):
    """
    Enum class for Vehicle type
    """
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

class ParkingSpotType(Enum):
    """
    Enum class for Parking spt
    """
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5

class Account:
    """
    Account Class
    """
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class Admin(Account):
    """
    Admin Class is a subclass of account class
    """
    pass
