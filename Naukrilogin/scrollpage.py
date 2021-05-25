from selenium import webdriver
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Login(object):
    def login(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://www.naukri.com/')
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,500)')
        time.sleep(2)
        driver.execute_script(('window.scrollTo(0,0)'))
        time.sleep(2)
        driver.execute_script('window.open()')
        time.sleep(7)
L=Login()
L.login()