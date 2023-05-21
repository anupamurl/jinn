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
 
 
driver.get('https://www.linkedin.com')
driver.find_element_by_pro('xcoJPARJg9creFi').click_pro()
driver.find_element_by_pro('ISw3KbGf_HX0PLb').type('mailsofmanisha@yahoo.com')
driver.switch_to.active_element.type('Tab')
driver.find_element_by_pro('bWpxjgudeyUVu7V').type('Anupam@294')    
driver.switch_to.active_element.type('Enter') 

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])  
def foo():
    print('request start')
    search = request.args.get("keyword")
    limitdata  =  request.args.get("limit" ,  type=int)  
    peoplekeyword = request.args.get("people")  
    url = "https://www.linkedin.com/search/results/content/?keywords="+str(search)     
    driver.get(url)
    time.sleep(20)
    src = driver.find_element_by_class_name('scaffold-finite-scroll__content').get_attribute('innerHTML')
     
 
    soup = BeautifulSoup(src, 'html.parser')    
    posts = []
    for li in soup.find_all('li' , limit= limitdata ):    
     
        com = li.find('div', {'class': 'update-components-text'}); 
        if com is not None:
         userlink = li.find('a', {'class': 'app-aware-link'}).get('href') 
         driver.get(userlink)
         time.sleep(5)
         peoplesrc = driver.find_element_by_class_name('pv-top-card').get_attribute('innerHTML')
         peoplesoup = BeautifulSoup(peoplesrc, 'html.parser')  
         userpost = {           
           'comment': li.find('div', {'class': 'update-components-text'}).text.strip(),
           'userlink' :  userlink,
           'username' :  peoplesoup.find('h1', {'class': 'text-heading-xlarge'}).text.strip() ,
           'designation' :  peoplesoup.find('div', {'class': 'text-body-medium'}).text.strip() ,
           'company' :  peoplesoup.find('span', {'class': 'pv-text-details__right-panel-item-text'}).text.strip()       ,
           'location'  :     peoplesoup.find(class_='pv-text-details__left-panel mt2').text.strip()  
            
            
                
         }
         posts.append(userpost)        
    return posts
if __name__ == '__main__':
 app.run(debug=False, port=8001)