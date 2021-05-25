from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
driver.get('https://letskodeit.teachable.com/')
print(driver.current_url)
driver.find_element_by_xpath('//a[@class=\'fedora-navbar-link navbar-link\']').click()
driver.implicitly_wait(10)
try:
    radiobutton=driver.find_element_by_xpath("//input[@id='bmwradio']")
    if radiobutton.is_enabled():
        print('Radio button is enabled')
        radiobutton.click()
    else:
        print('radio button is not enabled')

    print('Element found')
except:
    print('Element not found')
if radiobutton.is_selected():
    print('Radio button is selected')
else:
    print('radio button is not selected')
print(radiobutton.get_attribute('type'))
try:
    radiobuttonbenz=driver.find_element_by_xpath("//input[@id='benzradio']")
    print('Radio button name'+str(radiobutton.text))

except:
    print("element not found")
driver.close()