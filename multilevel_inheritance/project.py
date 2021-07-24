# in multi level inheritance, the class inherits the features of another derived class (child class) (parent -> child -> grand child)
class parent(object):

    def __init__(self):
        print('parent constructor')

    def display_p(self):
        print('parent class method')

class child(parent):

    def __init__(self):
        super(child, self).__init__()       # calling parent class constructor
        print('child constructor')

    def display_c(self):
        print('child class method')

class grandchild(child):

    def __init__(self):
        super(grandchild, self).__init__()   # calling child class constructor
        print('grand child constructor')

    def display_gc(self):
        print('Grand child class method')

obj_1=grandchild()
print('----')
obj_1.display_gc()
obj_1.display_c()
obj_1.display_p()
