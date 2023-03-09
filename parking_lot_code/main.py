from enum import Enum
from datetime import datetime
from abc import ABC, abstractmethod

class VehicleType(Enum):
    """
    Enum class for Vehicle type
    """
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

class ParkingSpotType(Enum):
    """
    Enum class for Parking spot
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
    # no need to initialise __init__ again here because there is nothing new we are doing in __init__
    # than the parents __init__. if __init__ is not defined parent's __init__ will be picked up
    
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
    
    def add_entrance_panel(self, entrance_panel: EntrancePanel) -> bool:
        """
        Function to add entrance panel
        """
        pass
    
    def add_exit_panel(self, exit_panel: ExitPanel):
        """
        Function to add exit panel
        """
        pass

class ParkingAttendant(Account):
    """
    Parking attendant class is a subclass of account class
    """
    # this init can also be removed as the current classes init and its
    # parent init are same. So when python is executing the code
    # if in current class -> python will not find the init -> then it 
    # will execute its parent's init method

    def process_parking_tickets(self, p: ParkingTicket) -> bool:
        """
        Process Parking ticket
        """
        pass

class ParkingTicket:
    """
    Class defining details of parking ticket
    """

    def __init__(self, number_plate:str, issue_time:datetime):
        self.number_plate = number_plate
        self.issue_time = issue_time

# Parking Spot is an abstract class
# lot of other class extend the Parking Spot class
class ParkingSpot(ABC):
    """
    Abstract class defining basic details of a parking spot
    """
    def __init__(self, id: str, type: ParkingSpotType):
        self.id = id
        self.is_free = True # initially(class initialisation) parking spot will be free
        self.vehicle = None # initially(class initialisation) no vehicle will be assigned
        self.type = ParkingSpotType

    def assign_vehicle(self,v: Vehicle):
        """
        assign a parking spot to vehicle v
        """
        if self.is_free:
            self.vehicle = v
            self.is_free = False
        else:
            raise Exception("Parking spots are not free")
    
    def remove_vehicle(self):
        """
        Remove vehicle from the parking spot
        """
        self.vehicle = None
        self.is_free = True

class HandicappedSpot(ParkingSpot):
  """
  Class for Handicapped spot
  """
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.HANDICAPPED)

class CompactSpot(ParkingSpot):
  """
  Class for Compact Spot
  """
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.COMPACT)

class LargeSpot(ParkingSpot):
  """
  Class for Large Spot
  """
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.LARGE)

class MotorbikeSpot(ParkingSpot):
  """
  Class for Motorbike Spot
  """
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.MOTORBIKE)

class ElectricSpot(ParkingSpot):
  """
  class for Electric Spot
  """
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.ELECTRIC)


class Vehicle(ABC):
    """
    Vehicle Abstract class defining all the details of a Vehicle
    """
    def __init__(self, number:int, type: VehicleType):
      self.number = number
      self.type = type
      self.parking_ticket = None

    @abstractmethod
    def assign_ticket(self, parking_ticket:ParkingTicket):
      """
      Assign ticket to a vehicle
      """
      self.parking_ticket = parking_ticket

class Car(Vehicle):
    def __init__(self, license_number):
       super().__init__(license_number, VehicleType.CAR)
    
    def assign_ticket(self, parking_ticket: ParkingTicket):
       return super().assign_ticket(parking_ticket)


class Van(Vehicle):
    def __init__(self, license_number):
       super().__init__(license_number, VehicleType.VAN)
    
    def assign_ticket(self, parking_ticket: ParkingTicket):
       return super().assign_ticket(parking_ticket)


class Truck(Vehicle):
    def __init__(self, license_number):
       super().__init__(license_number, VehicleType.TRUCK)
    
    def assign_ticket(self, parking_ticket: ParkingTicket):
       return super().assign_ticket(parking_ticket)


# similarly class can be made for other vehicle types also
# which extends the vehicle class
class ExitPanel:
   """
   Class defining details for exit panel
   """
   def __init__(self, id: str):
      self.id = id
   
   def accept_payment(self, ticket: ParkingTicket):
      # accept payment for this parking ticket
      # on exit panel customers can pay for the parking ticket
      pass
   

class EntrancePanel:
   """
   Class defining details of Entrance Panel
   """

   def __init__(self, id: str)


class ParkingLot:
    """
    Main class Parking Lot of this system
    This is a singleton class means that there is only one instance of ParkingLot in this whole system
    """