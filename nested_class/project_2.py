# class within a class is called as nested class or nesting of a class
class army(object):  # outer class
    def __init__(self):
        self.name='john'

    def display(self):
        print('User Name:', self.name)

    class gun():  # inner class
        def __init__(self):
            self.name='ak47'
            self.capacity='75 rounds'
            self.length='35.4 inch'
        
        def display(self):
            print('gun name:',self.name,'capacity:',self.capacity,'length:',self.length)


p1=army() #  cresting outer class object
p1.display()
p2=army().gun()  # creating inner class object 
print(p2.display())
