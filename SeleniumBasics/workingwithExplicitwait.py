from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from openpyxl import Workbook

class WorkwithExplicitwait(object):
    def explicitwaitpratice(self):
        driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.get('https://www.redbus.in/')
        search=driver.find_element_by_id('src')
        wait=WebDriverWait(driver,10, poll_frequency=2, ignored_exceptions=[ElementNotVisibleException,
                                                                            ElementNotSelectableException, NoSuchElementException])
        WB=open

        # goingto=driver.find_element_by_css_selector('button[aria-label="Going to"]')
        # checkin=driver.find_element_by_css_selector('#d1-btn')
        # checkout=driver.find_element_by_css_selector('#d1-btn')
        # goingto.send_keys('')
        wait.until(EC.element_to_be_clickable,(By.ID,'src')).click()




W=WorkwithExplicitwait()
W.explicitwaitpratice()

