# instance methods are the methods which act upon the instance variable of the class
# instance method need to know the memory address of the instance which is provided through self variable by default as first parameter for the instance method
# instance methods are bound to object of the class so we call instance method with object name
class calculator(object):

    def __init__(self): # constructor
        self.x=2  # instance variable
        self.z=3
    def show(self):
        print('My Calculator')

    def add(self,a,b):
        self.a=a
        self.b=b
        self.z=self.a+self.b+self.x
        return self.z

    def sub(self,a,b):
        self.a = a
        self.b = b
        self.z=self.a-self.b-self.x
        return self.z

cal_1=calculator()
print('\n---\n')
print(cal_1.show())

print('\n---\n')
print('Self variable z:',cal_1.z)
print('Addition',cal_1.add(2,2))
print('Subtraction',cal_1.sub(4,1))
print('\n---\n')

cal_2=calculator()
print('Self variable z:',cal_2.z)
print('Self variable x:',cal_2.x)
