# we can check the object passed to the method has the method being invoked or not
# hasattr() function is used to check whether the object has a method or not 
# syntax: hasattr(object, attribute)
# where attribute can be a method or variable. if it is found in the object then this method returns True else False

class duck:
    def walk(self):
        print('thapak  thapak  thapak  thapak')

class horse:
    def walk(self):
        print('tabdak  tabdak  tabdak  tabdak')

class cat:
    def talk(self):
        print('meow  meow  meow')

def myfunction(obj):  # fixing error using strong typing
    if hasattr(obj,'walk'):
        obj.walk()
    elif hasattr(obj,'talk'): # if talk method is exist in the class then call otherwise sorry 
        obj.talk()

d=duck()
myfunction(d)        

h=horse()
myfunction(h)

c=cat()
myfunction(c)