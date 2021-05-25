class Statetax(object):
    def __init__(self):
        print('This function is used to claculate the tax')
        self.stateswithtax = {'TS': 10, 'AP': 15, 'DELHI': 20, 'MP': 15}
        print(self.stateswithtax['AP'])

    def statetax(self, state, gross):
        try:
            if state in self.stateswithtax:
                netamount = gross - (gross * self.stateswithtax[state] / 100)
                taxamount = gross - netamount
                return taxamount
            else:
                print('invalid state')
        except:
            print('enter valid input')

c1=Statetax()
print(c1.statetax('MP', 0))
