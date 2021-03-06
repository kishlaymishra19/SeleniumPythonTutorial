'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''
import unittest
from selenium import webdriver
import pages
from excelUtils import Excel_Data

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
        init.driver.close()

    def PageLaunch(self):
        homePage=pages.HomePage(self.driver)
        print(self.driver.title)
        assert homePage.is_title_matches
        
    def SearchText(self):
        hp=pages.HomePage(self.driver)
        hp.search_text_element = "phone"
        hp.search_item()
        sr=pages.SearchResultsPage(self.driver)
        assert sr.is_results_found()
        
    def AddToCart(self):
        cart=pages.AddItemToCart(self.driver)
        cart.click_add_to_cart()

    def MoveToLogin(self):
        cartPopup=pages.AddToCartPopup(self.driver)
        cartPopup.click_checkout_button()
        
    def MoveToCheckOut(self):
        sp=pages.SignInPage(self.driver)
        sp.continue_to_checkout()
        
    def Checkout(self):
        cp=pages.CheckOutPage(self.driver)
        cp.enter_email_id(Excel_Data.get_data(self, 'Emailid'))
        cp.enter_first=Excel_Data.get_data(self, 'FirstName')
        cp.enter_last=Excel_Data.get_data(self, 'LastName')
        cp.enter_add=Excel_Data.get_data(self, 'Address')
        cp.enter_city=Excel_Data.get_data(self, 'City')
        cp.enter_country=Excel_Data.get_data(self, 'Country')
        cp.enter_state=Excel_Data.get_data(self, 'State')
        cp.enter_zip=Excel_Data.get_data(self, 'Pincode')
        cp.enter_phone=Excel_Data.get_data(self, 'PhoneNumber')
        cp.local_pickup()
        cp.payment_method_demo()  
        cp.place_order_note="this is my order note"
        cp.place_order()   
        
    def Invoice(self):
        inv=pages.Invoice_Page(self.driver)
        inv.update_invoice_number()
    
    def testCreateOrder(self):
        Test.PageLaunch(self)
        Test.SearchText(self)        
        Test.AddToCart(self)
        Test.MoveToLogin(self)
        Test.MoveToCheckOut(self)
        Test.Checkout(self)
        Test.Invoice(self)
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)