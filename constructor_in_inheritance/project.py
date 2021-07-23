# By default, The constructor in the parent class is available to the child class
class mobile:

    def __init__(self,c,s):
        self.color=c
        self.size=s
        print('Parent class constructor')

class model(mobile):

    # inheritance: We get the parent constructor, it is because we did not write any child class constructor otherwise child class constructor will be called
    mdl='nokia'

    def show(self):
        print('Color:',self.color,'\nSize:',self.size,'\nModel',model.mdl)

obj_1=model('black','5x3')
obj_1.show()


