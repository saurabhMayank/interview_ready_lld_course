

# main Function for calling handler
if __name__ == "__main__":
  main()


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

# singelton class implementation
class TextEditorSingleton:
    # class instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TextEditorSingleton, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance

    def __init__(self):
        pass
