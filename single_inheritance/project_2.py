# single inheritance
# if a class is derived from one base class (parent class), it is called single inheritance
class mobile:

    color='black'
    size='5x3'

    @classmethod
    def show(cls):
        print('Color:',cls.color,'\nSize:',cls.size)

    @staticmethod
    def stat():
        print('Welcome objects- Static Method')

class model(mobile):

    @classmethod
    def assign_model(cls, m):
        cls.mdl=m

    @classmethod
    def show(cls):
        print('Color:',model.color,'\nSize:',model.size,'\nModel:',cls.mdl)

model.assign_model('nokia')
obj_1=model()
obj_1.stat()
obj_1.show()
