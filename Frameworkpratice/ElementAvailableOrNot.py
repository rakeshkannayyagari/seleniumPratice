from selenium import webdriver

class ElementAvailableOrNot(object):
    def __init__(self, element='//a[@class=\'fedora-navbar-link navbar-link\']'):
        self.element= element
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        self.driver.get('https://letskodeit.teachable.com/')
        self.driver.implicitly_wait(10)

    def  availableOrNot(self):
         try:
             praticebutton=self.driver.find_element_by_xpath(self.element)
             praticebutton.click()
             self.driver.implicitly_wait(10)
             currentURL = str(self.driver.current_url)
             print(currentURL)
             try:
                 assert currentURL=='https://letskodeit.teachable.com/'
                 print('element found')
                 print('Assertion passed')
             except:
                 print('element found')
                 print('Assertion failed')
         except:

             print('element not found')

c1=ElementAvailableOrNot()
c1.availableOrNot()
