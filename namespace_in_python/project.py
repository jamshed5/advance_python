#namespace
'''
In python, namespace represents a memory block, where names are mapped to
objects

class namespace:
a class maintains its own namespace knowns as class
namespace. in the class namespace, the name are mapped 
to class variables 

Instance namespace 
every instance/object have its own namespace knowns as instance
namespace. in the instance namespace, the names are mapped 
to instance variables 
'''
class mobile:
    model='nokia'
   
    @classmethod
    def display(cls):
        print('Model is:',cls.model)

obj1=mobile()
obj2=mobile()
obj3=mobile()

print(mobile.model)
print(obj1.model)
print(obj2.model)
print(obj3.model)

print('-----')

mobile.model='samsung'

print(mobile.model)
print(obj1.model)
print(obj2.model)
print(obj3.model)

print('-----')

obj2.model='iphone'

print(mobile.model)
print(obj1.model)
print(obj2.model)
print(obj3.model)
