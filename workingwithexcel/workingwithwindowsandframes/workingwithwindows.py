from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

class MultipleWindows(object):
    def windowhanderespratice(self):
        wb=openpyxl.load_workbook('sample.xlsx')
        ws1=wb.active
        site=ws1.cell(1,1).value
        print(site)
        driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.maximize_window()
        driver.get(site)
        driver.execute_script("window.open('http://www.seleniumframework.com/Practiceform/');")
        driver.execute_script('window.open()')
        driver.get_screenshot_as_file('photo.png')
        time.sleep(5)
        driver.close()
        time.sleep(5)
        # currentwindow=driver.current_window_handle
        # print(currentwindow)
        # print('Before switch: '+str(driver.title))
        # driver.find_element_by_css_selector('#button1').click()
        # driver.find_element_by_css_selector('button[onclick="newBrwTab()"]').click()
        # totalwindows=driver.window_handles
        # print(len(totalwindows))
        #
        # afterswitch=driver.switch_to_window(driver.window_handles[1])
        # print(driver.current_window_handle)
        # print('After switch: ' + str(driver.title))
        # time.sleep(5)
        # driver.minimize_window()
        # driver.get('https://www.browserstack.com/guide/how-to-switch-tabs-in-selenium-python')
        # time.sleep(5)
        #
        # afterswitch = driver.switch_to_window(driver.window_handles[2])
        # print(driver.current_window_handle)
        # print('After switch: ' + str(driver.title))
        # time.sleep(5)
        # driver.maximize_window()
        # driver.get('https://www.browserstack.com/guide/how-to-switch-tabs-in-selenium-python')
        # time.sleep(5)

        # for window in allwindows:
        #     if window is not currentwindow:
        #         driver.switch_to_window(driver.window_handles[1])
        #         afterswitch=driver.current_window_handle
        #         driver.maximize_window()
        #         print(afterswitch)
        #         break



M1=MultipleWindows()
M1.windowhanderespratice()

