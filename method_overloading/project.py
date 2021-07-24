# method overloading
'''
when more than one method with the same name is defined in the same class its is
known as method overloading but this behavior is not exist in python.

In python, if a method is written such that it can perform more than one task, it 
is called method overloading
'''
class calculator:
    def sum(self,a=None,b=None,c=None):
        
        if a!=None and b!=None and c!=None:
            self.z=a+b+c

        elif a!=None and b!=None:
            self.z=a+b
    
        return self.z

obj=calculator()

# same function but working for different number of arguments 

print(obj.sum(2,2,2)) 

print(obj.sum(2,2))

