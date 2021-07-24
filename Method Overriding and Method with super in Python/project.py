# Method overriding 
'''
if we write method in the both classes,parent class and child then the parent class's
method is not available to the child class
in this case only child class's method is accessible which means child class's
method is replacing parent class's method 
method overriding is used when programmer want to modify the existing behavior 
of a method 
'''
# super() method
'''
if we write method in the both classes, parent class and child class then the 
parent class's method is not availabe to the child class
in this case only child class's method is accessible which means child class's
method is replacing parent class's method 
supper() method is used to call parent class constructor or methods from the 
child class
'''
class calculator:
    
    def result(self, a,b):
        return a+b

class sub_cal(calculator):

    def result(self,a,b):  # same method (like outer class) but overriding (this time multiplication)
        sum=super().result(a,b) 
        return a*b, sum

obj_1=sub_cal()

print(obj_1.result(2,3))
