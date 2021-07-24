# Static methods are used when some processing is related to the class but does not need the class or its instance to perform any work
# We use static method when we want to pass some values from outside and perform some action in the method
# static method can access class variable
class calculator:
    c=2
    @staticmethod # decorator
    def add(a,b):
        z=a+b+calculator.c # getting class variable (remember that this is not class method, so will not be used cls.c)
        return z

cal_1=calculator()
print('Addition:',calculator.add(2,2)) # calling static method using class name
print('Class variable:',calculator.c)