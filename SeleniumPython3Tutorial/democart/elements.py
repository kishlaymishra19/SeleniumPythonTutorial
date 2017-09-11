'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''

from selenium.webdriver.support.ui import WebDriverWait
from pip.utils.filesystem import check_path_owner

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