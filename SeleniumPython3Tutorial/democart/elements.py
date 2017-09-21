'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''

from selenium.webdriver.support.ui import WebDriverWait

class HomePageElements(object):
    
    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements_by_xpath(self.locator))
        driver.find_elements_by_xpath(self.locator)[0].send_keys(value)
        
    def __get__(self, obj,check_path_owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_elements_by_xpath(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
    

class CheckOutPageElements(object):
    def __set__(self,obje,value):
        driver=obje.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        if (self.locator!='shippingaddress-country-code'):
            driver.find_element_by_id(self.locator).send_keys(value)
        elif(self.locator!='shippingaddress-state-id'):
            driver.find_element_by_id(self.locator).send_keys(value)
        elif(self.locator!='email'):
            driver.find_element_by_id(self.locator).clear()
            driver.find_element_by_id(self.locator).send_keys(value)
        else:
            driver.find_element_by_id(self.locator).clear()
            driver.find_element_by_id(self.locator).send_keys(value)

class CheckOutPageClickableElements(object):
    def __set__(self,oBj,value):
        driver=oBj.driver
        WebDriverWait(driver,100).until(
            lambda driver: driver.find_element_by_id(self.locator))
        self.driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element_by_id(self.locator))
        self.driver.execute_script("window.scrollBy(0, -150);")
        driver.find_element_by_id(self.locator).click()