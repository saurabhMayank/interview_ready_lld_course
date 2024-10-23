

# main Function for calling handler
if __name__ == "__main__":
  main()

# use class method to access class variable
"""
No, you should not use a static method to access or modify class variables. Instead, you should use a class method (@classmethod) for this purpose.

Why Not Use Static Methods for Modifying Class Variables?
Static Methods Lack Access to Class Context: Static methods do not receive any reference to the class (cls) as the first parameter, which means they do not have direct access to the class attributes or methods. They act like regular functions that happen to be within the class namespace.
No Access to Class State: Without the cls parameter, static methods cannot access or modify class-level variables. You would have to reference the class name explicitly, which is less flexible and not suitable for inheritance.
Use Class Methods to Access and Modify Class Variables
Class methods are designed to operate on the class itself rather than on an instance of the class. They receive the class (cls) as the first argument, allowing them to access and modify class variables.
"""
class Example:
    class_variable = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    @classmethod
    def set_class_variable(cls, value):
        cls.class_variable = value

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

# Example usage
print(Example.get_class_variable())  # Outputs: 0

Example.increment_class_variable()
print(Example.get_class_variable())  # Outputs: 1

Example.set_class_variable(10)
print(Example.get_class_variable())  # Outputs: 10


"""
Generating auto increment Ids
"""
class Question:
  # question number should auto increment
  question_data = []
  current_id = 0

  def __init__(self, name, level, marks):
    self.id = Question._generate_id()
    self.name = name
    self.level = level
    self.marks = marks


  @classmethod
  def _generate_id(cls):
    # Auto-increment the ID
    cls.current_id += 1
    return cls.current_id



# time library
import time

# Pause execution for 100 seconds
time.sleep(100)

print("100 seconds have passed.")

# timestamp
time.time()


import random

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

 numbers = []
    while len(numbers) < k:
        num = random.randint(1, 6)
        if num not in numbers:
            numbers.append(num)
    return numbers


# use of data time library
from datetime import datetime, timedelta

# Initialize the start time
start_time = datetime.now()
print(f"Start Time: {start_time}")

# Function to add minutes to the start time
def add_minutes_to_time(time, minutes):
    return time + timedelta(minutes=minutes)

# Example: Adding 15 minutes to the start time
time_after_15_minutes = add_minutes_to_time(start_time, 15)
print(f"Time After 15 Minutes: {time_after_15_minutes}")

# Check if the current time has reached or exceeded the time limit
current_time = datetime.now()
if current_time >= time_after_15_minutes:
    print("Time limit reached or exceeded")
else:
    print("Time limit not yet reached")


# use of giving start_time & end_time of a schedule
from datetime import datetime, timedelta

def schedule_meeting(start_hours, start_minutes, duration_hours):
    # Parse the start time
    start_time = datetime.now().replace(hour=start_hours, minute=start_minutes, second=0, microsecond=0)

    # Calculate the end time
    end_time = start_time + timedelta(hours=duration_hours)

    return start_time, end_time

# abstrac class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage:
rect = Rectangle(4, 5)
print(rect.area())  # Output: 20

# enumerate
# gives index to each item while printing it
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# static methods
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

result = MathUtils.add(5, 3)
print(result)  # Output: 8



# tuples
# Creating a pair
point = (3, 4)  # Represents a point with x=3, y=4

# Accessing elements
x_coordinate, y_coordinate = point
print(x_coordinate, y_coordinate)  # Output: 3 4

my_tuple = (1, 2, 3, "hello")
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3


# enum 
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def check_valid_color(color_input):
    return color_input in Color

user_input = Color.RED
if check_valid_color(user_input):
    print("Valid color")
else:
    print("Invalid color")


# json

import json

# Sample JSON string
data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Parse JSON into Python dictionary
python_data = json.loads(data)
print(python_data)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York'}

# Access data from the dictionary
print(python_data['name'])  # Output: John Doe

# Create a Python dictionary
my_data = {'name': 'Alice', 'age': 25, 'is_student': True}

# Convert Python dictionary to JSON string
json_data = json.dumps(my_data)
print(json_data)  # Output: {"name": "Alice", "age": 25, "is_student": true}



# Design patterns

"""
The Singleton pattern ensures only one instance of the class exists.
__new__ controls the creation of the instance, while __init__ ensures that initialization only 
happens once.

*args, **kwargs -> pass in new to support to any number of args passed due to
instance instialisation

__init__ will only be called when _initialised attribute not part of self
rest other times it will not be called

The pattern allows you to pass arguments during the first instantiation, 
but subsequent instantiations return the same object without reinitializing it.
"""

# singelton class implementation
class DemoSingleton:
    # class instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DemoSingleton, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance

    def __init__(self, argument):
        if not hasattr(self, '_initialized'):
            self.arg = argument
            self._initialized = True



# Decorator Pattern

from abc import ABC, abstractmethod

# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.0  # Base price for simple coffee

    def description(self) -> str:
        return "Simple Coffee"


# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.5  # Additional cost for milk

    def description(self) -> str:
        return self._coffee.description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5  # Additional cost for sugar

    def description(self) -> str:
        return self._coffee.description() + ", Sugar"

class VanillaDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 2.0  # Additional cost for vanilla syrup

    def description(self) -> str:
        return self._coffee.description() + ", Vanilla"

# Create a simple coffee
coffee = SimpleCoffee()
print(coffee.description())  # Outputs: Simple Coffee
print(coffee.cost())  # Outputs: 5.0

# Add milk to the coffee
coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.description())  # Outputs: Simple Coffee, Milk
print(coffee_with_milk.cost())  # Outputs: 6.5

# Add sugar to the coffee with milk
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_and_sugar.description())  # Outputs: Simple Coffee, Milk, Sugar
print(coffee_with_milk_and_sugar.cost())  # Outputs: 7.0

# Add vanilla to the coffee with milk and sugar
coffee_with_everything = VanillaDecorator(coffee_with_milk_and_sugar)
print(coffee_with_everything.description())  # Outputs: Simple Coffee, Milk, Sugar, Vanilla
print(coffee_with_everything.cost())  # Outputs: 9.0



# Good Error handling mechanism to use in Python

raise ValueError -> when proper values are not passed in the argument
raise IndexError -> when trying to access an invalid index
raise SyntaxError -> for invalid syntaxes
