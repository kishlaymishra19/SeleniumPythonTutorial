'''
Created on Sep 11, 2017

@author: kishlay.mishra
'''
from selenium.webdriver.common.by import By


class HomePageLocators(object):
    GO_BUTTON = (By.XPATH, "//input[@placeholder='Search items...']")

class SearchResultsPageLocators(object):
    SEARCH_RESULT=(By.XPATH,"//ul[@class='products-grid grid-list']/li")
    ADD_TO_CART_BUTTON=(By.XPATH,"//span[text()='Add to cart']")
    
class AddToCartPopupLocators(object):
    CHECKOUT_BUTTON=(By.XPATH,"//*[@id='ui-id-3']/div/div/div/div[1]/div[6]/a[2]/span")
    CART_BUTTON=(By.XPATH,"//div[@id='ui-id-5']//div[@class='item-buttons']/a[1]")
    PAY_WITH_PAYPAL=(By.XPATH,"//div[@id='ui-id-5']//div[@class='pp-button']/button")
    
class PostSignInPageLocators(object):
    EMAIL_INPUT=(By.NAME,"email")
    CONTINUE_BUTTON=(By.XPATH,"//span[text()='Continue']")
    
class CheckOutPageLocators(object):
    PLACE_ORDER_BUTTON=(By.XPATH,"//button[@class='btn  regular-button regular-main-button place-order submit']/span")
    EMAIL_TEXT_BOX=(By.ID,"email")
    DELIVERY_METHOD_LOCAL_PICKUP=(By.XPATH,'//*[@id="method8"]')
    PAYMENT_METHOD_DEMO=(By.XPATH,"//span[text()='X-Payments DEMO']")