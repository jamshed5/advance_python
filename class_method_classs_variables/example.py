# class method, class variable, inheritance (& calling class methods and variables using class name)
# also possible by using instance of the class but we are using class method so having a specific reasons
class calculator(object):
    # initializing class variable z (its possible to access with in class method)
    z=0
    @classmethod
    def show(cls):
        print('My Calculator')

    @classmethod # decorator
    def add(cls,a,b):
        cls.a=a
        cls.b=b
        cls.z=cls.a+cls.b
        return cls.z

    @classmethod  # decorator
    def sub(cls,a,b):
        cls.a = a
        cls.b = b
        cls.z=cls.a-cls.b
        return cls.z

class advance_calculator(calculator):
    @classmethod
    def mul(cls,a,b):
        cls.a=a
        cls.b=b
        cls.z=cls.a*cls.b
        return cls.z

cal_1=advance_calculator()
print(advance_calculator.show())
print('\n---\n')
print('Class variable:',advance_calculator.z)
print('Multiplication',advance_calculator.mul(2,2))
print('Addition',advance_calculator.add(2,2))
print('Subtraction',advance_calculator.sub(2,2))

print('\n---\n')
cal_2=advance_calculator()
print('Class variable:',cal_2.z)
print('Multiplication',cal_2.mul(2,2))
print('Addition',cal_2.add(2,2))
print('Subtraction',cal_2.sub(2,2))

print('\n---\n')
cal_3=advance_calculator()
print('Class variable:',cal_3.z)

print('\n---\n')
cal_4=advance_calculator()
print('Class variable:',cal_4.z)
