class WarperClassesGetelement():
    def __init__(self,driver):
        self.driver = driver
    #dropdownelement=driver.find_element_by_link_text('Dropdown')

    def getElementAndConvert(self,element,elementtype):
        elementtype=elementtype.lower()

        if elementtype == 'id':
            return self.driver.find_element_by_id(element)
        elif elementtype == 'name':
            return self.driver.find_element_by_name(element)
        elif elementtype == 'xpath':
            return self.driver.find_element_by_xpath(element)
        elif elementtype == 'css':
            return self.driver.find_element_by_css_selector(element)
        elif elementtype == 'linktext':
            return self.driver.find_element_by_link_text(element)
        elif elementtype == 'partiallinktext':
            return self.driver.find_element_by_partial_link_text(element)
        elif elementtype == 'class':
            return self.driver.find_element_by_class_name(element)
        elif elementtype == 'tag':
            return self.driver.find_element_by_tag_name(element)
        else:
            print("element type is invalid")
