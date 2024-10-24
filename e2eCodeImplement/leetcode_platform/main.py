# coding platform machine coding
"""
Requirements

https://github.com/hocyadav/leetcode-lld-flipkart-coding-blox

This link has the complete requirements
"""




import time


"""
Models
"""

class LEVEL(Enum):

  LOW = 1
  MEDIUM = 2
  HARD = 3

class CONTEST_STATUS(Enum):
  CREATED = 1
  STARTED = 2
  ONGOING = 3
  ENDED = 4



class User:
  users_data = []
  def __init__(self, name: str):
    self.id = time.time()
    self.name = name
    self.total_score = 0
  
  def add_new_user(cls, user):
    """
    Add new user to user_data
    """
    cls.user_data.append(user)
  
  def update_user_score(cls, user, new_score):
    for user_val in users_data:
      if user_val.id == user.id:
        user_val.total_score = new_score
        user.total_score = new_score
        break
    
    return user
  
  
class Contest:
  contest_data = []
  current_id = 0

  def __init__(self, name: str, level:LEVEL ):
    self.id = Contest._generate_id()
    self.name = name
    self.level = level
    self.status = CONTEST_STATUS.CREATED
  
  @classmethod
  def _generate_id(cls):
    # Auto-increment the ID
    cls.current_id += 1
    return cls.current_id

  
  def add_new_contest(cls, contest):
    """
    Add new contest
    """
    cls.contest_data.append(contest)
  
  def update_contest_level(cls, contest, level):
    for contest_obj in cls.contest_data:
      if contest_obj.id == contest.id:
        contest_obj.level = level
        contest.level = level 
        break
    
    return contest
  
  def update_contest_status(cls, contest, status):
    for contest_obj in cls.contest_data:
      if contest_obj.id == contest.id:
        contest_obj.status = status
        contest.status = status 
        break
    
    return contest

  def filter_contest_by_difficulty(cls, difficulty_level):
    contest_list = []
    for cont in cls.contest_data:
      if cont.difficulty_level == difficulty_level:
        contest_list.append(cont)
    
    return contest_list

class UserContest:
  user_contest_data = []

  def __init__(self, user, contest):
    self.id = time.time()
    self.user = user
    self.contest = contest
  
  def add_user_contest_data(cls, user_contest):
    cls.user_contest_data.append(user_contest)

  def get_user_contest_by_user(cls, user):
    user_cont_list = []
    for user_contest in user_contest_data:
      if user_contest.user.id == user.id:
        user_cont_list.append(user_cont_list)
    
    return user_cont_list
  

  def get_user_contest_by_contest(cls, contest):
    user_cont_list = []
    for user_contest in user_contest_data:
      if user_contest.contest.id == contest.id:
         user_cont_list.append(user_cont_list)
    
    return user_cont_list


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
  
  
  def add_question_data(cls, question):
    cls.question_data.append(question)
  
  def get_all_ques(cls):
    return cls.question_data
  
  def filter_ques_by_difficulty(cls, difficulty_level):
    ques_list = []
    for ques in question_data:
      if ques.difficulty_level == difficulty_level:
        ques_list.append(ques)
    
    return ques_list


  
  def change_question_level(cls, question, level):
    for ques in question_data:
      if ques.id == queston.id:
        ques.level = level
        question.level = level
        break
    
    return question


class ContestQuestion:
  contest_ques_data = []
  def __init__(self, question, contest):
    self.id = time.time()
    self.question = question
    self.contest = contest
  

  def add_contest_ques_data(cls, contest_ques):
    cls.contest_ques.append(contest_ques)

  
  def get_contest_ques_by_ques(cls, question):
    cont_ques = []
    for contest_ques in cls.contest_ques_data:
      if contest_ques.question.id == question.id:
        cont_ques.append(contest_ques)
    
    return cont_ques
  
  def get_contest_ques_by_contest(cls, contest):
    cont_ques = []
    for contest_ques in cls.contest_ques_data:
      if contest_ques.contest.id == contest.id:
        cont_ques.append(contest_ques)
    
    return cont_ques




"""
Services
"""

class UserService:
  def __init__(self):
    pass
  
  def add_user(self, name):
    user_obj = User(name)

    User.add_new_user(user_obj)

    return user_obj


class ContestService:
  def __init__(self):
    pass
  
  def create_contest(self, contest_name, contest_lvl: Level, contest_creator):

    # create contest model
    contest_model = Contest(name, contest_lvl)

    Contest.add_new_contest(contest_model)

    # create user<>contest model
    # contest creator will definitely attend the contest
    user_contest_model = UserContest(contest_creator, contest_model)

    UserContest.add_user_contest_data(user_contest_model)

    return contest_model


  def list_contest(self, contest_lvl: Level):
    return Contest.filter_contest_by_difficulty(contest_lvl)







class QuestionService:
  def __init__(self):
    pass
  
  def add_question(self,name, difficulty_level: LEVEL, marks):
    ques = Question(name, difficulty_level, marks)
    Question.add_question_data(ques)
    return ques
  
  def filter_queslist_by_difficulty(self, difficulty_level):
    return Question.filter_ques_by_difficulty(difficulty_level)

  


  



"""
Api Handler
"""



"""
Main function
"""




if __name__ == "__main__":
  main()