'''
polymorphism is a word that come from two geek words, poly means many and
morphoes means forms.
if a variable, object or method perform differet behavior according to 
sistuation, it is called polymorphism
- duck typing
- operator overloading
- method overloading
- method overriding 
'''

# duck typing 
'''
In python , we follow a prinicple - if' it walks like a duck and talk like a duck
it must be duck' which means python does not care about which class of 
object its is, if it is an object and required behavior is present for that object
then it will work. The type of object is distinguished only at runtime.
This is called as duck typing

python doesnot care about which class of object its is, in order to call an
existing method on an object. if the method is defined on the object, then it 
will be called.
'''


class duck:
    def walk(self):
        print('thapak  thapak  thapak  thapak')

class horse:
    def walk(self):
        print('tabdak  tabdak  tabdak  tabdak')

class cat:
    def talk(self):
        print('meow  meow  meow')

def myfunction(obj):  # here method is dont know which class object will be there, and it will work if funcationaly is exist otherwise user get error
    obj.walk()

d=duck()
myfunction(d)        

print('----------NOW GET EEOR BCZ CAT OBJECT HAS NO WALK METHOD--------')

c=cat()
myfunction(c)