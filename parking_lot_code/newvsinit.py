class A:
    def __new__(cls, *args, **kwargs):
        print('new', cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('init', self, args, kwargs)


def how_object_construction_works():
    x = A(1, 2, 3, x=4)

    # above is equivalent to below, but this can be customized using metaclasses
    # When x = A(1,2, 3, x=4) is called
    # then __new__ method is called -> which creates instance of the class
    # after that if the instance created of the type expected
    # then init method initalizes the instance with default and sets up 
    # other things on the created instance

    # new always returns the instance created
    # init on the other hand -> does not return anything

    x = A.__new__(A, 1, 2, 3, x=4)
    if isinstance(x, A):
        type(x).__init__(x, 1, 2, 3, x=4)
    print(x)


# new is generally used to subclass builtin immutable datatypes
# once builtin datatypes are created they cannot be changed

# Like example of having upper class keys in the tuple
# Once the tuple is created u cannot modify it

# this will give an error when you try to modify the immutable tuple
class UppercaseTuple(tuple):
    # Error: tuples are immutable, even in init
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()

# but when creating the tuple in the first place
# we can intercept its creation and change the implementation using __new__
# Note: Instance can be created inside __new__ method by using super function
# instance = super(MyClass, cls).__new__(cls, *args, **kwargs)
# in the new versions of python
# super(MyClass, cls).__new__(cls, *args, **kwargs) == super().__new__(cls, *args, **kwargs)

class UppercaseTuple(tuple):
    def __new__(cls, iterable):
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)

    # Error: tuples are immutable, even in init
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()