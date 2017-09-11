'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''
import unittest
from selenium import webdriver
import pages

class Test(unittest.TestCase):


    @classmethod
    def setUpClass(init):
        init.driver=webdriver.Chrome("C:\\Users\\kishlay.mishra\\Downloads\\chromedriver.exe")
        init.driver.implicitly_wait(10)
        init.driver.maximize_window()
        init.driver.get("https://demostore.x-cart.com/")


    @classmethod
    def tearDownClass(init):
        print("Test Ended")
#        init.driver.close()

    def test1PageLaunch(self):
        homePage=pages.HomePage(self.driver)
        print(self.driver.title)
        assert homePage.is_title_matches
        
    def test2SearchText(self):
        hp=pages.HomePage(self.driver)
        hp.search_text_element = "phone"
        hp.search_item()
        sr=pages.SearchResultsPage(self.driver)
        assert sr.is_results_found()
        
    def test3AddToCart(self):
        cart=pages.AddItemToCart(self.driver)
        cart.click_add_to_cart()

    def test4MoveToLogin(self):
        cartPopup=pages.AddToCartPopup(self.driver)
        cartPopup.click_checkout_button()
        
    def test5MoveToCheckOut(self):
        sp=pages.SignInPage(self.driver)
        sp.continue_to_checkout()
    
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)