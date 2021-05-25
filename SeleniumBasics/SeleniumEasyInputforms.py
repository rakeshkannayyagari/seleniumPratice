from SeleniumBasics.Browseropen import BrowserOpen
from SeleniumBasics.searchforproduct import SearchforProduct
from SeleniumBasics.Signinpage import Loginpage

class SeleniumEasyInputformsSampleformDemo(BrowserOpen):
    def inputformsSampleformDemo(self,searchcriteria1,searchcriteria2):
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(10)
        '''
        title=self.driver.title
        if title=='My Store':
            print('Title of the site is '+title)
        else:
            print('Title is failed original title is '+title)
        print("searching with " + searchcriteria1)
        SearchforProduct.searching(self,searchcriteria1)
        SearchforProduct.backToHome(self)
        print("searching with " + searchcriteria2)
        SearchforProduct.searching(self, searchcriteria2)
        SearchforProduct.backToHome(self)'''
        Loginpage.logintoapplication(self)
        self.driver.close()


C1=SeleniumEasyInputformsSampleformDemo()
C1.inputformsSampleformDemo("Men","dress")

