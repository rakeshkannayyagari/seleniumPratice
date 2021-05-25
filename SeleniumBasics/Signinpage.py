from SeleniumBasics.Browseropen import BrowserOpen
from selenium.webdriver.common.by import By
from SeleniumBasics.searchforproduct import SearchforProduct
class Loginpage(BrowserOpen):
    def logintoapplication(self):
        loginpagebuton='//a[@class="login"]'
        loginpagebutonelement=self.driver.find_element(By.XPATH,loginpagebuton)
        # print('Attribate name is '+loginpagebutonelement.get_attribute('type'))
        loginpagebutonelement.click()
        emailaddress=self.driver.find_element(By.XPATH,'//input[@id="email"]')
        password=self.driver.find_element(By.XPATH,'//input[@id="passwd"]')
        signin = self.driver.find_element(By.XPATH, '//a[@class ="icon-lock left"]')
        signin.click()
        alertmessage=self.driver.find_element(By.XPATH,'//div[@id="center_column"]/div[@class="alert alert-danger"]')
        print('When no user name and password entered alert message is displaying as '+ alertmessage.text)
        SearchforProduct.backToHome(self)
        loginpagebutonelement.click()
        self.driver.implicitly_wait(10)
        emailaddress.send_keys('Ramesh')
        signin.click()
        print('Alert message when user id is provided '+alertmessage.text)
        self.driver.implicitly_wait(10)
        SearchforProduct.backToHome(self)
        self.driver.implicitly_wait(10)
        loginpagebutonelement.click()
        self.driver.implicitly_wait(10)
        emailaddress.clear()
        emailaddress.send_keys("Vanitha")
        password.send_keys('password')
        signin.click()
        print('Alert message when user id and password is provided ' + alertmessage.text)
