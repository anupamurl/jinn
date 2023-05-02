import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import json
from selenium_pro import webdriver
from selenium_pro.webdriver.support.ui import WebDriverWait
from selenium_pro.webdriver.support import expected_conditions as EC
from selenium_pro.webdriver.common.by import By
import numpy as np
driver = webdriver.Start()
# driver.get('https://www.linkedin.com/jobs/search/?keywords=cyber%20security%20analyst')
# driver.find_element_by_pro('76KNymy0OD1r15G').click_pro()
# src = driver.find_element_by_class_name('jobs-search__results-list').get_attribute('innerHTML')
# with open("keyword.txt",'w') as f:
#   f.write(src)

 
jobs = [{'jobtitle': 'Tier 1 SOC Analyst', 'cname': 'Fusion Technology LLC', 'clogo': 'https://media.licdn.com/dms/image/C510BAQGwbSzcFn8mRQ/company-logo_100_100/0/1519876137403?e=2147483647&v=beta&t=wZ5LGE3qxim8yasQnrvQKFbYX6EU4RHD093SebYGH0k', 'location': 'Boulder, CO', 'time': '1 month ago', 'link': 'https://www.linkedin.com/jobs/view/tier-1-soc-analyst-at-fusion-technology-llc-3580768661', 'companylink': '/company/fusion-technology-llc/life/', 'cinfo': []}]
     
driver.get('https://www.linkedin.com')
driver.find_element_by_pro('xcoJPARJg9creFi').click_pro()
driver.find_element_by_pro('ISw3KbGf_HX0PLb').type('8595704389')
driver.switch_to.active_element.type('Tab')
driver.find_element_by_pro('bWpxjgudeyUVu7V').type('Payal@209')    
driver.switch_to.active_element.type('Enter') 
        
for obj in jobs:
    obj['companylink'] = "https://www.linkedin.com"+obj['companylink'].replace('/life', '')
    obj['companyabout'] =   obj['companylink']+"about"
    obj['companyceo'] =    obj['companylink']+"people/?keywords=ceo"
    driver.get(obj['companyabout']) 
    # element = WebDriverWait(driver, 10).until(
    #                   EC.presence_of_element_located((By.CLASS_NAME, "jobs-unified-top-card"))
    #         )   
      
print(jobs)    