'''
Created on May 9, 2018

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
opt.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\kishlay.mishra\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
chrome_path='C:\\Users\\kishlay.mishra\\Downloads\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(chrome_path,chrome_options=opt)
driver.implicitly_wait(15)
driver.get("http://www.seleniumhq.org/download/")
driver.find_element_by_link_text("32 bit Windows IE").click()