from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Login(object):
    def login(self):

        driver = webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.maximize_window()
        driver.get('https://s1.demo.opensourcecms.com/wordpress/')
        driver.implicitly_wait(10)
        wait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[ElementNotSelectableException,
                                                                          ElementNotVisibleException,
                                                                          NoSuchElementException,
                                                                          InvalidElementStateException])
        element=wait.until(EC.NoSuchElementException,(By.CSS_SELECTOR,'.id'))
        loginlink = driver.find_element_by_link_text('Log in')
        if loginlink is not None:
            print('Log in link is found')
            print(loginlink.text)
            print(loginlink.get_attribute('innerText'))
            loginlink.click()
            print(driver.title)
        else:
            print('Log in loin link is not found')

        username =driver.find_element_by_css_selector('#user_login')
        password =driver.find_element_by_css_selector('.password-input')

        if username is not None:
            print("User name found")
            print(username.text)
            print((username.get_attribute('value')))
            username.send_keys('opensourcecms')
        else:
            print('Username is not found')

        if password is not None:
            print('Password is found')
            print(password.text)
            password.send_keys('opensourcecms')
        else:
            print('Password not found')

        loginbutton=driver.find_element_by_css_selector("[name='wp-submit']")
        if loginbutton is not None:
            print('Login button is found')
            print(loginbutton.get_attribute('value'))

            loginbutton.click()
        else:
            print('Login button not found')

l=Login()
l.login()
