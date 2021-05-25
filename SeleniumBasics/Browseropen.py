from selenium import webdriver

class BrowserOpen(object):
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        self.driver.maximize_window()
