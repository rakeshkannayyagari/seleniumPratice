from SeleniumBasics.Browseropen import BrowserOpen
from selenium.webdriver.common.by import By
class SearchforProduct(BrowserOpen):

    def searching(self,searchcriteria):
        searchelementXpath = '//input[@id="search_query_top"]'
        searchbuttonxpath = '//button[@name="submit_search"]'
        searchElementLocater = self.driver.find_element(By.XPATH, searchelementXpath)
        searchbuttonlocater = self.driver.find_element(By.XPATH, searchbuttonxpath)
        if searchElementLocater is not None:
            print('Search text element is  found and entering search criteria')
            searchElementLocater.send_keys(searchcriteria)
            if searchbuttonlocater is not None:
                print('Search button found and clicking on it')
                searchbuttonlocater.click()
                searchresultsxpath = '//span[@class="heading-counter"]'
                searchresultslocater = self.driver.find_element(By.XPATH, searchresultsxpath)
                print('Number of results are ' + searchresultslocater.text)
                print("User is in search results page and title is " + self.driver.title)
            else:
                print('Search button is not found')
        else:
            print('Search element is not found')
    def backToHome(self):
        backtohomexpath='//a[@class="home"]'
        backtohomelocater=self.driver.find_element(By.XPATH,backtohomexpath)
        backtohomelocater.click()
        print("User is in home page and title is "+self.driver.title)