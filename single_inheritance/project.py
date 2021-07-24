# single inheritance
# if a class is derived from one base class (parent class), it is called single inheritance
class mobile:

    color='black'
    size='5x3'

    def show(self):
        print('Color:',mobile.color,'\nSize:',mobile.size)

    @staticmethod
    def stat():
        print('Welcome objects- Static Method')

class model(mobile):

    def __init__(self,m):
        self.model=m

    def show(self): # override method
        print('Color:', model.color, '\nSize:', model.size, '\nModel:', self.model)


obj_1=model('Nokia')
obj_1.stat()
obj_1.show()

