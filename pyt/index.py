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

# https://www.linkedin.com/search/results/content/?keywords=looking%20for%20ux%20designer&origin=SWITCH_SEARCH_VERTICAL&sid=Hm2
#driver = webdriver.Start()
# driver.get('https://www.linkedin.com/jobs/search/?keywords=cyber%20security%20analyst')
# driver.find_element_by_pro('76KNymy0OD1r15G').click_pro()
# src = driver.find_element_by_class_name('jobs-search__results-list').get_attribute('innerHTML')
# with open("keyword.txt",'w') as f:
#   f.write(src)
 
 
jobs = [{'jobtitle': 'Tier 1 SOC Analyst', 'cname': 'Fusion Technology LLC', 'clogo': 'https://media.licdn.com/dms/image/C510BAQGwbSzcFn8mRQ/company-logo_100_100/0/1519876137403?e=2147483647&v=beta&t=wZ5LGE3qxim8yasQnrvQKFbYX6EU4RHD093SebYGH0k', 'location': 'Boulder, CO', 'time': '1 month ago', 'link': 'https://www.linkedin.com/jobs/view/tier-1-soc-analyst-at-fusion-technology-llc-3580768661', 'companylink': 'https://www.linkedin.com/company/fusion-technology-llc/', 'cinfo': ['\n\n\n\n\n\n\n\n\n\n\nContract · Entry level\n\n', '\n\n\n\n\n\n\n\n\n\n\n51-200 employees · IT Services and IT Consulting\n\n', '\n\n\n\n\n\n\n\n\n\n\nSee how you compare to 26 applicants. Try Premium for free\n\n'], 'companyabout': 'https://www.linkedin.com/company/fusion-technology-llc/about', 'companyceo': 'https://www.linkedin.com/company/fusion-technology-llc/people/?keywords=ceo', 'aboutcompany': 'Trust must be earned through consistent performance. All of us at Fusion Technology understand the importance of an individual commitment to excellence. This foundational understanding and guiding belief in providing unparalleled IT support services has enabled us to establish a reputation as a dependable performer in our industry. \n\nFor more than a decade, Fusion Technology has been providing IT services and solutions to various governmental agencies, private organizations, government contractors, healthcare facilities, and corporations, providing high quality service and support in many disciplines. \n\nFusion Technology works with the government and private sectors, providing a full range of IT services and solutions to ensure U.S. national security. With decades of experience in the Federal IT space and a commitment to excellence, we strive to bring success to each of our clients by using industry best practices and best value solutions. \n\nFounded in 2007, we created our business because we realized that there was a better, more efficient way to provide IT services and solutions. By investing in our employees and understanding their value, not only do we retain highly skilled, motivated employees, we also produce results that go beyond our client’s expectations. With this foundation in place, Fusion Technology is one of the fastest growing small businesses in the information technology field. \n\nWe value our employees. By providing excellent benefit choices to employees and their families and creating a sense of community within the company, we make sure to invest in the success of our employees. ', 'companyattr': {'Id': ['Website', 'Industry', 'Company size', 'Headquarters', 'Founded', 'Specialties'], 'Attribute': ['http://www.fusiontechnology-llc.com', 'IT Services and IT Consulting', '51-200 employees', '119 on LinkedIn\n            \n \n\n\n\n    Includes members with current employer listed as Fusion Technology LLC, including part-time roles.', 'Bridgeport, West Virginia', '2007', 'Information Technology Services, Information Technology Operations, System Engineering, Software Development, Cloud , Biometrics, Cybersecurity, Data Analytics, Geospatial, Enterprise Search, and Identity and Access Management']}}]

 
# driver.get('https://www.linkedin.com')
# driver.find_element_by_pro('xcoJPARJg9creFi').click_pro()
# driver.find_element_by_pro('ISw3KbGf_HX0PLb').type('mailsofmanisha@yahoo.com')
# driver.switch_to.active_element.type('Tab')
# driver.find_element_by_pro('bWpxjgudeyUVu7V').type('Anupam@294')    
# driver.switch_to.active_element.type('Enter') 
# for obj in jobs:
# #  driver.get(obj['companyceo']) 
# #  element = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.CLASS_NAME, "scaffold-finite-scroll__content"))
# #     )    

# data = driver.find_element_by_class_name('scaffold-finite-scroll__content').get_attribute('innerHTML')  

with open('people.txt') as f:
    src = f.read()   
    soup = BeautifulSoup(src, 'html.parser')
    
    ceos = []
    for li in soup.find_all('li'):
       info = { }      
       people = li.find( class_ = "org-people-profile-card__profile-title" ) 
       if people is not None:
              info['name'] = people.text.strip()
       else:
              info['name'] = "No Data Found"  

       linkedlink = li.find( class_ = "app-aware-link" ) 
       if linkedlink is not None:
              info['link'] = linkedlink.get('href') 
       else:
              info['link'] = "No Data Found"  
                 
       ceos.append(info)
    print(ceos)   