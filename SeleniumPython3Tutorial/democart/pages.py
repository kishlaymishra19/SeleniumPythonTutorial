'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''

from elements import HomePageElements
from locator import HomePageLocators
from locator import SearchResultsPageLocators
from locator import AddToCartPopupLocators
from locator import PostSignInPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class SearchTextElement(HomePageElements):
    locator="//input[@placeholder='Search items...']"
    
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
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "0 products found" not in self.driver.page_source
    

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