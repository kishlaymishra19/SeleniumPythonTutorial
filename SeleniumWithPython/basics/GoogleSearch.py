'''
Created on Apr 10, 2018

@author: kishlay.mishra
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

opt=webdriver.ChromeOptions()
opt.add_argument('--disable-extensions')
opt.add_argument('--start-maximized')
opt.add_argument('disable-infobars')
opt.add_argument('--ignore-certificate-errors')
opt.add_argument("--test-type")
chrome_path='C:\\Users\\kishlay.mishra\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(chrome_path,chrome_options=opt)
driver.implicitly_wait(15)
driver.get("http://www.google.com")
print(driver.title)
elem = driver.find_element_by_name("q")
elem.send_keys("Kishlay Mishra")
elem.send_keys(Keys.RETURN)
resultCount=driver.find_element_by_id("resultStats")
print(resultCount.text)
driver.close()
driver.quit()
