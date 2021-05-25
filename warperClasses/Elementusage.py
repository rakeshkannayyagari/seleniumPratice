from selenium import webdriver
from warperClasses.warperclassesgetelement import WarperClassesGetelement

class UsingElements(object):
    def usingelemsntsfromwarper(self,element,elementtype):
        driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.implicitly_wait(5)
        wp=WarperClassesGetelement(driver)
        dropdown=wp.getElementAndConvert(element,elementtype)
        dropdown.click()
u=UsingElements()
u.usingelemsntsfromwarper('Dropdown','linktext')
