class SealingFan(object):
    def __init__(self, company, color, status='available',  makeyear='2021' ):
        self.manufacturedcompany=company
        self.color=color
        self.available=status
        self.makeyear=makeyear

    def info(self):
        print('Requested Fan is a sealing fan, manufactured by '+self.manufacturedcompany+ ' available in '+self.color+' color '+
              ' currently stock is '+self.available+' make year is '+self.makeyear)
    def getorder(self):
        print("Get the order from customer")

    def packorder(self):
        self.getorder()
        print('Pack required number of orders')

    def delever(self):
        self.packorder()
        print('Delever the order')

c1=SealingFan('Usha','Black')
c1.info()
c1.getorder()
