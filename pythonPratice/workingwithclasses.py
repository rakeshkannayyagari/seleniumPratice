class SealingFan(object):
    def __init__(self, company, color, status='no',  makeyear ='2021' ):
        self.manufacturedcompany = company
        self.color = color
        self.available = status
        self.makeyear = makeyear

    def info(self):
        print('Requested Fan is a sealing fan, manufactured by '+self.manufacturedcompany+ ' available in '+self.color+' color '+
              ' currently stock is '+self.available+' make year is '+self.makeyear)
    def getorder(self):
        print("Get the order from customer")

    def delever(self):
        self.getorder()
        if self.available.upper()=='YES':
            print('Pack required number of orders')
            print('Delever the order')

        elif self.available.upper()=='NO':
            print('Stock is not avalable')

        else:
            print('you have not entered valid input')

class TableFan(SealingFan):
    def __init__(self, company, color, status,  makeyear ='2021' ):
        print('This is table fan')
        SealingFan.__init__(self, company, color, status,  makeyear ='2021' )

c1=SealingFan('Usha','Black','yes','1990')
c1.info()
c1.delever()
print('************************')
c2=TableFan('Crompton','white','yes')
c2.delever()