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
    currentwindow=driver.current_window_handle
    driver.switch_to_window(currentwindow)
    driver.implicitly_wait(10)
    # wait.until(EC.NoSuchElementException, (By.CSS_SELECTOR, 'a[data-ga-track="Main Navigation Jobs|Jobs Icon"]'))
    # jobscss =driver.find_element_by_css_selector('a[data-ga-track="Main Navigation Jobs|Jobs Icon"]')
    # jobsmove=action.move_to_element(jobscss)
    # jobsmove.perform()
    # time.sleep(3)
    # wait.until(EC.NoSuchElementException,(By.CSS_SELECTOR,'a[data-ga-track="Main Navigation Recruiters|Recruiters Icon"]'))
    # recuterscss=driver.find_element(By.CSS_SELECTOR,'a[data-ga-track="Main Navigation Recruiters|Recruiters Icon"]')
    # recutersmove=action.move_to_element(recuterscss).perform()
    time.sleep(3)
    allheaders=driver.find_elements_by_xpath('//ul[@class="midSec menu"]/li')
    print(len(allheaders))
    for i in allheaders:
        print(i)
        moveheader=action.move_to_element(i).perform()
        time.sleep(2)
        continue
        print(i.get_attribute('innerText'))

    # alllinksunderrecuter=driver.find_elements_by_xpath('//ul[@class="midSec menu"]/li[2]/div[@class="subMenu"]/ul/li')
    # print(len(alllinksunderrecuter))
    # for i in alllinksunderrecuter:
    #     moverecuters=action.move_to_element(i).perform()
    #     print(i.get_attribute('innerText'))
    #     time.sleep(2)

    driver.quit()


