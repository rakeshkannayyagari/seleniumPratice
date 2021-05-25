class Car(object):
    wheels=4
    stearing=1
    doors=4

    def __init__(self, name='Indica', brand='Tata', origion='India'):
        self.nameofcar=name
        self.nameofbrand=brand
        self.nameofcountry=origion

    def info(self):
        print('My car name is '+ self.nameofcar+' , it is manufactured by '+ self.nameofbrand+ ' and the company is from '+self.nameofcountry)
        print('My car is having '+str(self.wheels)+' wheels, '+str(self.stearing)+' stearing and '+str(self.doors)+' doors')

    def startthecar(self):
        print('Start the engine so my car '+self.nameofcar+ ' is started')

    def pressbreak(self):
        self.startthecar()
        print('Press the break')

    def stopcar(self):
        self.pressbreak()
        print('stop the engine')

class Tata(Car):
    def __init__(self,name,brand,origion):
        Car.__init__(self,name,brand,origion)
        print("my Tata car is manufactured")


c1=Car('BMW', 'Tata', 'India')
c1.info()
c1.stopcar()
