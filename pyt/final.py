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
        driver.find_element_by_pro('ISw3KbGf_HX0PLb').type('mailsofmanisha@yahoo.com')
        driver.switch_to.active_element.type('Tab')
        driver.find_element_by_pro('bWpxjgudeyUVu7V').type('Anupam@294')    
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
            obj['companylink'] = "https://www.linkedin.com"+obj['companylink'].replace('/life', '')
            obj['companyabout'] =   obj['companylink']+"about"
            obj['companyceo'] =    obj['companylink']+"people/?keywords=ceo"
            driver.get(obj['companyabout']) 
            element = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.CLASS_NAME, "application-outlet"))
            ) 
            aboutsrc  = driver.find_element_by_class_name('application-outlet').get_attribute('innerHTML')   
            aboutsoup = BeautifulSoup(aboutsrc, 'html.parser')   
            srcfile =  aboutsoup.find('section', {'class': 'artdeco-card p5 artdeco-card mb4'})
            first_inner_p = srcfile.find('p')
            if first_inner_p is not None:
              obj['aboutcompany'] = first_inner_p.getText()
            else:
             obj['aboutcompany'] = "No Data Found"
            info = srcfile.find("dl" )

            comp_info  = {}
            cleaned_id_text = []
            for i in info.find_all('dt'):
                cleaned_id_text.append(i.text.strip())
            cleaned_id__attrb_text = []
            for i in info.find_all('dd'):
                cleaned_id__attrb_text.append(i.text.strip())

            comp_info['Id'] = cleaned_id_text
            comp_info['Attribute'] = cleaned_id__attrb_text
          
            obj['companyattr'] = comp_info


    print(jobs) 
    with open("jobwithlink.txt",'w') as f: 
     f.write(str(jobs))
         