'''
Created on May 9, 2018

@author: kishlay.mishra
'''
from selenium import webdriver

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
driver.get("http://demo.guru99.com/test/upload/")
driver.find_element_by_name('uploadfile_0').send_keys('C:\\Users\\kishlay.mishra\\Pictures\\report.png')
driver.find_element_by_id('terms').click()
driver.find_element_by_id('submitbutton').click()
driver.save_screenshot('uploadScreenshot.png')