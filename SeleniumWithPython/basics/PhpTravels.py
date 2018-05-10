'''
Created on Apr 14, 2018

@author: kishlay.mishra
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt=webdriver.ChromeOptions()
opt.add_argument('--disable-extensions')
opt.add_argument('--start-maximized')
opt.add_argument('disable-infobars')
opt.add_argument('--ignore-certificate-errors')
opt.add_argument("--test-type")
chrome_path='C:\\Users\\kishlay.mishra\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(chrome_path,chrome_options=opt)
driver.implicitly_wait(15)
driver.get("http://www.phptravels.net/")
assert 'PHPTRAVELS' in driver.title

driver.find_element_by_partial_link_text('MY ACCOUNT').click()
driver.find_element_by_partial_link_text('Login').click()

driver.find_element_by_name('username').send_keys('user@phptravels.com')
driver.find_element_by_name('password').send_keys('demouser')
driver.find_element_by_class_name('loginbtn').click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID,'preloader'))
        #EC.presence_of_element_located((By.XPATH, "//span[text()='All listed prices are based on realtime']"))
    )
finally:
    print(driver.title)

driver.find_element_by_xpath("//a[@title='Hotels']/span[contains(text(),'Hotels')]").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID,'preloader'))
        #EC.presence_of_element_located((By.XPATH, "//span[text()='All listed prices are based on realtime']"))
    )
finally:
    print(driver.title)

driver.find_element_by_xpath("//h4[@class='RTL go-text-right mt0 list_title']/a").click()
roomName=driver.find_element_by_xpath("//b[text()='Junior Suites']")
driver.execute_script("arguments[0].scrollIntoView();", roomName)
driver.find_element_by_xpath("//b[text()='Junior Suites']/ancestor::td//button[text()='Book Now']").click()

driver.execute_script("arguments[0].scrollIntoView();",driver.find_element_by_xpath("//button[text()='CONFIRM THIS BOOKING']"))
driver.find_element_by_xpath("//button[text()='CONFIRM THIS BOOKING']").click()