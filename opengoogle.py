import time
import selenium
from selenium import webdriver
driver = webdriver.Firefox()
#Webdriver obj, loads Firefox()
driver.get("http://www.google.com")
#Open URL
time.sleep(60)
#Wait 60 seconds
driver.quit()
#Close all open automated tabs
