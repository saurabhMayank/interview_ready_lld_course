# coding platform machine coding
import time


"""
Models
"""

class LEVEL(Enum):

  LOW = 1
  MEDIUM = 2
  HARD = 3

class STATUS(Enum):
  STARTED = 1
  ONGOING = 2
  ENDED = 2



class User:
  users_data = []
  def __init__(self, name: str):
    self.id = time.time()
    self.name = name
    self.score = 0
  
  def add_new_user(cls, user):
    """
    Add new user to user_data
    """
    cls.user_data.append(user)
  
  def update_user_score(cls, user, new_score):
    for user_val in users_data:
      if user_val.id == user.id:
        user_val.score = new_score
        user.score = new_score
  
  
class Contest:
  contest_data = []

  def __init__(self, name: str, level:LEVEL, status:  ):
    self.id = time.time()
    self.name = name
    self.level = level
    self.status = 


"""
Services
"""



"""
Api Handler
"""



"""
Main function
"""




if __name__ == "__main__":
  main()