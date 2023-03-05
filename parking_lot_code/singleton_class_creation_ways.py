# python module stating different ways
# in which singleton class can get instantiated

# Way 1
class Singleton:
    # Class variable to store the singleton instance
    # Class variables are directly accessed by ClassName.VariableName
    __instance = None

    # lazy instantiation of singleton
    # when user calls get_instance
    # at that time only the Singleton instance is initialised
    # There will only one singleton instance that can be there
    # So a if check is put in place to check if singleton instance
    # has been initialised or not
    # Singelton instance will only be initialised if it has not been
    # done till now
    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    # In java for creating singleton class
    # Constructor is made private so that
    # from no-where in the system user can 
    # create an object of the class
    # here in python things are in a different way
    # Inside init which is the constructor
    # we check if Singleton instance has not been created
    # i.e. class variable __instance is None or not
    # if it is not None -> raise Exception -> Users cannot directly create object of this class

    # If Singleton.__instance is None means get_instance() is getting called for the first time
    # save the instance i.e. self in Singleton.__instance

    # def __init__(self):
    #     if Singleton.__instance != None:
    #         raise Exception("Singleton class already exists! Use Singleton.get_instance() to access it")
    #     else:
    #         Singleton.__instance = self
        


s1 = Singleton.get_instance()
print(s1)
s2 = Singleton.get_instance()
print(s2)
# s3 = Singleton()
# print(s3)
# s4 = Singleton()
# print(s4)


# Way 2 => Here get_instance is not used

class Singleton:
    # class variable is accessed using cls inside dunder method __new__
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

s1 = Singleton()
s2 = Singleton()


# __new__ creates the instance and returns it to __init__
# so intercepting the instance creation in the __new__ method
# if cls.__instance is empty => then create the new instance and store it in cls.__instance
# if cls.__instance is not empty => then return the same instance
# in this way => There is only one instance always => that is used every time Singelton class is initialised
# New instances are not created when singelton class is initialised
