from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


import time

class WorkingwithElements(object):
    def workingwithcheckbox(self):
        driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        dropdownelement=driver.find_element_by_link_text('Dropdown')
        option=Select(dropdownelement)
        option.select_by_index(0)
        option.select_by_index(1)


        # checkbox=driver.find_element_by_link_text('Checkboxes')
        # checkbox.click()
        # checkboxelements=driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
        # checkboxlenth=len(checkboxelements)
        # print('Number of check boxes available are '+str(checkboxlenth))
        # #Selecting check boxes
        #
        # for selectingcheckbox in checkboxelements:
        #     if not selectingcheckbox.is_selected():
        #         print('Selecting check box '+selectingcheckbox.text)
        #         selectingcheckbox.click()
        #         time.sleep(3)
        #     else:
        #         print('Checkbox is already selected'+selectingcheckbox.text)
        #




c1=WorkingwithElements()
c1.workingwithcheckbox()

