from selenium import webdriver
class openBrowser(object):
    def chromebrowser(self):
        driver=webdriver.Chrome(executable_path='C:\\Users\\rakes\\Desktop\\chromedriver.exe')
        driver.maximize_window()

    def fireFoxBrowser(self):
        driver=webdriver.Firefox(executable_path='C:\\Users\\rakes\\Desktop\\geckodriver.exe')
        driver.maximize_window()



cc=openBrowser()
cc.chromebrowser()