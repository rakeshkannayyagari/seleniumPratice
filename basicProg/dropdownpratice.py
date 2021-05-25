from selenium import webdriver
from selenium.webdriver.support.select import Select
class workingondropdown():
    def dropdownpratice(self):
        driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.get('https://letskodeit.teachable.com/p/practice')
        alldropdowns=driver.find_elements_by_tag_name('option')
        dropdownvalues=Select(driver.find_element_by_id('carselect'))
        dropdownvalues.select_by_index(0)
        dropdownvalues.select_by_index(1)
        dropdownvalues.select_by_index(2)
        print(dropdownvalues.all_selected_options)
dd=workingondropdown()
dd.dropdownpratice()

