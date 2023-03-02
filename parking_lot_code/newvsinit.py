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


# new is generally used to subclass immutable datatypes