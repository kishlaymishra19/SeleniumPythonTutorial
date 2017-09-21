'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''

from elements import HomePageElements
from elements import CheckOutPageElements
from selenium.webdriver.support.ui import WebDriverWait
from locator import HomePageLocators
from locator import SearchResultsPageLocators
from locator import AddToCartPopupLocators
from locator import PostSignInPageLocators
from locator import CheckOutPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time
from excelUtils import Excel_Data

class SearchTextElement(HomePageElements):
    locator="//input[@placeholder='Search items...']"
    
class Enter_Email(CheckOutPageElements):
    locator='email'
    
class Enter_First(CheckOutPageElements):
    locator='shippingaddress-firstname'

class Enter_Last(CheckOutPageElements):
    locator='shippingaddress-lastname'
    
class Enter_Add(CheckOutPageElements):
    locator='shippingaddress-street'
    
class Enter_City(CheckOutPageElements):
    locator='shippingaddress-city'
    
class Enter_Country(CheckOutPageElements):
    locator='shippingaddress-country-code'
    
class Enter_State(CheckOutPageElements):
    locator='shippingaddress-state-id'
    
class Enter_Zip(CheckOutPageElements):
    locator='shippingaddress-zipcode'
    
class Enter_Phone(CheckOutPageElements):
    locator='shippingaddress-phone'
    
class Bill_Add(CheckOutPageElements):
    locator='same_address'

class Place_Order_Note(CheckOutPageElements):
    locator='place_order_note'    
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "X-Cart Demo store company > Catalog" in self.driver.title

    def search_item(self):
        """Triggers the search"""
        elementList = self.driver.find_elements(*HomePageLocators.GO_BUTTON)
        elementList[0].submit()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        return "0 products found" in self.driver.page_source
    

class AddItemToCart(BasePage):
    def click_add_to_cart(self):
        results=self.driver.find_elements(*SearchResultsPageLocators.SEARCH_RESULT)
        addToCartButton=self.driver.find_element(*SearchResultsPageLocators.ADD_TO_CART_BUTTON)
        ActionChains(self.driver).move_to_element(results[0]).click(addToCartButton).perform()

class AddToCartPopup(BasePage):
    def click_checkout_button(self):
        self.driver.find_element(*AddToCartPopupLocators.CHECKOUT_BUTTON).click()      
    def click_Viewcart_button(self):
        self.driver.find_element(*AddToCartPopupLocators.CART_BUTTON).click()    
    def click_paypal_button(self):
        self.driver.find_element(*AddToCartPopupLocators.PAY_WITH_PAYPAL)
        
class SignInPage(BasePage):
    def continue_to_checkout(self):
        self.driver.find_element(*PostSignInPageLocators.EMAIL_INPUT).send_keys('ok@ok.com') 
        self.driver.find_element(*PostSignInPageLocators.CONTINUE_BUTTON).click()
        
class CheckOutPage(BasePage):
    enter_email=Enter_Email()
    enter_first=Enter_First()
    enter_last=Enter_Last()
    enter_add=Enter_Add()
    enter_city=Enter_City()
    enter_country=Enter_Country()
    enter_state=Enter_State()
    enter_zip=Enter_Zip()
    enter_phone=Enter_Phone()
    place_order_note=Place_Order_Note()
    
    bill_add=Bill_Add()
    def wait_for_loader(self):
        try:
            print("Checking for loader")
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.wait-block-overlay")))
        except Exception:
            print("Loader not found")
        else:
            print("Loader found")
    def place_order(self):
        try:
            CheckOutPage.wait_for_loader(self)
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,"//button[@class='btn  regular-button regular-main-button place-order submit']/span")))
            CheckOutPage.wait_for_loader(self)
            self.driver.find_element(*CheckOutPageLocators.PLACE_ORDER_BUTTON).click()
            CheckOutPage.wait_for_loader(self)
            CheckOutPage.wait_for_loader(self)
        except WebDriverException:
            CheckOutPage.wait_for_loader(self)
            self.driver.find_element(*CheckOutPageLocators.PLACE_ORDER_BUTTON).click()
            CheckOutPage.wait_for_loader(self)
        
    def enter_email_id(self,val):
        self.driver.find_element(*CheckOutPageLocators.EMAIL_TEXT_BOX).clear()
        self.driver.find_element(*CheckOutPageLocators.EMAIL_TEXT_BOX).send_keys(val)
    def local_pickup(self):
        deliver_button=self.driver.find_element(*CheckOutPageLocators.DELIVERY_METHOD_LOCAL_PICKUP)
        self.driver.execute_script("return arguments[0].scrollIntoView();", deliver_button)
        self.driver.execute_script("window.scrollBy(0, -150);")
        self.driver.find_element(*CheckOutPageLocators.DELIVERY_METHOD_LOCAL_PICKUP).click()
        CheckOutPage.wait_for_loader(self)
    def payment_method_demo(self):
        time.sleep(5)
        CheckOutPage.wait_for_loader(self)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH,"//span[text()='X-Payments DEMO']")))
        CheckOutPage.wait_for_loader(self)
        self.driver.find_element(*CheckOutPageLocators.PAYMENT_METHOD_DEMO).click()
        CheckOutPage.wait_for_loader(self)
        
class Invoice_Page(BasePage):
    def update_invoice_number(self):
        val=self.driver.find_element_by_class_name('invoice').text
        Excel_Data.write_result(self, val)
        print("Entered excel data: "+val)