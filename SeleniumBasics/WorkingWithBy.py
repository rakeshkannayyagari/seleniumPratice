from selenium import webdriver
from selenium.webdriver.common.by import By

class WorkingwithBy(object):
    def __init__(self):
        baseURL='https://letskodeit.teachable.com/p/practice'
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        self.driver.get(baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def checkBoxselection(self):
        bmwCheckboxXpath="//div[@id='checkbox-example']//label[@for='bmw']"
        benzCheckboxXpath="//div[@id='checkbox-example']//label[@for='benz']"
        hondaCheckboxXpath="//div[@id='checkbox-example']//label[@for='honda']"
        try:
            bmwCheckboxelement=self.driver.find_element(By.XPATH,bmwCheckboxXpath)
            if bmwCheckboxelement.is_enabled():
                print('BMW check box is enabled ')
                # verifying check box is selected or not
                if bmwCheckboxelement.is_selected():
                    print('BMW check box is selected ')
                else:
                    print('BMW check box is not selected so selecting check box')
                    bmwCheckboxelement.click()
                    if bmwCheckboxelement.is_selected():
                        print('BMW check box is selected ')
                    else:
                        print('BMW check box is not selected so selecting check box')
            else:
                print('BMW check box is not enabled')
        except:
            print('BMW Element not found')

        try:
            hondaCheckboxelement=self.driver.find_element(By.XPATH,hondaCheckboxXpath)
            if hondaCheckboxelement.is_enabled():
                print('Honda check box is enabled ')
                # verifying check box is selected or not
                if hondaCheckboxelement.is_selected():
                    print('Honda check box is selected ')
                else:
                    print('Honda check box is not selected so selecting check box')
                    hondaCheckboxelement.click()
                    if hondaCheckboxelement.is_selected():
                        print('Honda check box is selected ')
                    else:
                        print('Honda check box is not selected so selecting check box')
            else:
                print('Honda check box is not enabled')
        except:
            print('Honda Element not found')
        try:
            benzCheckboxelement=self.driver.find_element(By.XPATH,benzCheckboxXpath)
            if benzCheckboxelement.is_enabled():
                print('Benz check box is enabled ')
                # verifying check box is selected or not
                if benzCheckboxelement.is_selected():
                    print('Benz check box is selected ')
                else:
                    print('Benz check box is not selected so selecting check box')
                    benzCheckboxelement.click()
                    if benzCheckboxelement.is_selected():
                        print('Benz check box is selected ')
                    else:
                        print('Benz check box is not selected so selecting check box')
            else:
                print('Benz check box is not enabled')
        except:
            print('Benz Element not found')
        self.driver.close()

c1=WorkingwithBy()
c1.checkBoxselection()