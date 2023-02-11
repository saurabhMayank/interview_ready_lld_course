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
    # this init can also be removed as the current classes init and its
    # parent init are same. So when python is executing the code
    # if in current class -> python will not find the init -> then it 
    # will execute its parent's init method
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
    
    # passed here ParkingLot ka instance because we are treating ParkingLot as a singleton class
    # singleton class cannot be instantiated, it has a single static instance
    def add_parking_floor(self, parking_floor: ParkingFloor, parking_lot:ParkingLot) -> bool:
        """
        Function to add parking floor
        """
        pass

    def add_parking_spot(self, parking_floor: ParkingFloor, parking_spot: ParkingSpot) -> bool:
        """
        Function to add parking spot
        """
        pass

    def add_parking_display_board(self, parking_floor: ParkingFloor, display_board: ParkingDisplayBoard) -> bool:
        """
        Function to add parking spot
        """
        pass
    
    