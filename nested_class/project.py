# class within a class is called as nested class or nesting of a class
class army(object):  # outer class
    def __init__(self):
        self.name='john'
        self.g_obj=self.gun()

    def display(self):
        print('User Name:', self.name)

    class gun():  # inner class
        def __init__(self):
            self.name='ak47'
            self.capacity='75 rounds'
            self.length='35.4 inch'
        
        def display(self):
            print('gun name:',self.name,'capacity:',self.capacity,'length:',self.length)

p1=army()
p1.display()
p1.g_obj.display()

print('-----')

print('inner class object:',p1.g_obj)
print('-----')

print('capacity:',p1.g_obj.capacity)  # geeting getting inner class variable , as we have alreadying creating inner class object in outer class constructor 