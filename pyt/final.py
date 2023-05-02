import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import json
from selenium_pro import webdriver
from selenium_pro.webdriver.support.ui import WebDriverWait
from selenium_pro.webdriver.support import expected_conditions as EC
from selenium_pro.webdriver.common.by import By
 
driver = webdriver.Start()
# driver.get('https://www.linkedin.com/jobs/search/?keywords=cyber%20security%20analyst')
# driver.find_element_by_pro('76KNymy0OD1r15G').click_pro()
# src = driver.find_element_by_class_name('jobs-search__results-list').get_attribute('innerHTML')
# with open("keyword.txt",'w') as f:
#   f.write(src)


 


with open('keyword.txt') as f:
    src = f.read()   
    soup = BeautifulSoup(src, 'html.parser')
    
    jobs = []
    for li in soup.find_all('li'):
       
        imgsrc =  li.find( 'img' , {'class': 'artdeco-entity-image'})
        time_tag =  li.find('time', {'class': 'job-search-card__listdate'})
        if time_tag is not None:
           time_tag =  li.find('time', {'class': 'job-search-card__listdate'})
        else:          
            time_tag =  li.find('time', {'class': 'job-search-card__listdate--new'})
        
        parsed_url = urlparse( li.find('a', {'class': 'base-card__full-link'}).get('href')  )
        query_dict = parse_qs(parsed_url.query)    
        job = {           
        'jobtitle': li.find('span', {'class': 'sr-only'}).text.strip(),
        'cname': li.find( 'a' , {'class': 'hidden-nested-link'}).text.strip(),
        'clogo':  imgsrc.get('src')  , 
        'location':  li.find('span', {'class': 'job-search-card__location'}).text.strip(), 
        'time':  time_tag.text.strip(), 
         'link': parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path
        }
        jobs.append(job)
        driver.get('https://www.linkedin.com')
        driver.find_element_by_pro('xcoJPARJg9creFi').click_pro()
        driver.find_element_by_pro('ISw3KbGf_HX0PLb').type('8595704389')
        driver.switch_to.active_element.type('Tab')
        driver.find_element_by_pro('bWpxjgudeyUVu7V').type('Payal@209')    
        driver.switch_to.active_element.type('Enter') 
        for obj in jobs:
            driver.get(obj['link']) 
            element = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.CLASS_NAME, "jobs-unified-top-card"))
            )            
            jobsrc  = driver.find_element_by_class_name('jobs-unified-top-card').get_attribute('innerHTML')                      
            jobsoup = BeautifulSoup(jobsrc, 'html.parser')
            obj['companylink']  = jobsoup.find_all('a')[0].get("href")
            ul_elements = jobsoup.find_all('ul')
            li_texts = []
            for ul in ul_elements:
             li_elements = ul.find_all('li')
             for li in li_elements:
               li_texts.append(li.get_text())            
            obj['cinfo']  = li_texts 
 

    print(jobs) 
    with open("jobwithlink.txt",'w') as f: 
     f.write(str(jobs))
         