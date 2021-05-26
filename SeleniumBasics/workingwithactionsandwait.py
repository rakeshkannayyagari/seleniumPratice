from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Actionwait():
    driver = webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.naukri.com/')
    wait=WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[(NoSuchElementException,
                                                                        ElementNotVisibleException,
                                                                        ElementNotSelectableException,
                                                                        NoAlertPresentException)])
    action=ActionChains(driver)
    #driver.implicitly_wait(10)
    wait.until(EC.NoSuchElementException, (By.CSS_SELECTOR, 'a[data-ga-track="Main Navigation Jobs|Jobs Icon"]'))
    jobscss =driver.find_element_by_css_selector('a[data-ga-track="Main Navigation Jobs|Jobs Icon"]')
    jobsmove=action.move_to_element(jobscss)
    jobsmove.perform()

    time.sleep(10)
    driver.quit()


