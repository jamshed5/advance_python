# super() method is used to call parent class constructor or methods from the child class.
class mobile:

    def __init__(self,m):
        self.money=m
        print('Parent class constructor & money',self.money)

class model(mobile):

    def __init__(self):
        super().__init__(m=200) # calling parent class constructor and also i am passing argument
        self.money = 500
        print('Sun class constructor & money', self.money)


obj_1=model()



