import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import json
from selenium_pro import webdriver
from selenium_pro.webdriver.support.ui import WebDriverWait
from selenium_pro.webdriver.support import expected_conditions as EC
from selenium_pro.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import socketio
# sio = socketio.Client()
# sio.connect('http://localhost:3100')

driver = webdriver.Start()
url = "https://www.g2.com/categories/testing-and-qa"  
driver.get(url)
time.sleep(10)
src =  driver.find_element_by_class_name('review-filter-form-get').get_attribute('innerHTML')

#driver.find_element_by_xpath('//div[@aria-live="polite"]')
soup = BeautifulSoup(src, 'html.parser')    
print(soup)

print( 

 soup.find(class_='m-0 fw-regular').text.strip() 
)



    