# constructor overriding
# If we write constructor in the both classes, parent class and child class then the parent class constructor is not available to the child class
# In this case only child class constructor is accessible which means child class constructor is replacing parent class constructor
# Constructor overriding is used when programmer wants to modify the existing behavior of a constructor
class mobile:

    def __init__(self):
        self.money=200
        print('Parent class constructor & money',self.money)

class model(mobile):

    def __init__(self):
        self.money = 500
        print('Sun class constructor & money', self.money)

obj_1=model()



