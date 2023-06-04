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
sio = socketio.Client()
sio.connect('http://localhost:3100')
from multiprocessing import Process
from multiprocessing import parent_process
import re


# driver = webdriver.Start()
# driverkeyword = webdriver.Start() 
# driver.get('https://www.linkedin.com')
# time.sleep(5)
# driver.find_element_by_pro('xcoJPARJg9creFi').click_pro()
# driver.find_element_by_pro('ISw3KbGf_HX0PLb').type('mailsofmanisha@yahoo.com')
# driver.switch_to.active_element.type('Tab')
# driver.find_element_by_pro('bWpxjgudeyUVu7V').type('Anupam@294')    
# driver.switch_to.active_element.type('Enter') 


postdriver = webdriver.Start() 
postdriver.get('https://www.linkedin.com')
time.sleep(3) 
postdriver.find_element_by_pro('xcoJPARJg9creFi').click_pro()
postdriver.find_element_by_pro('ISw3KbGf_HX0PLb').type('8595704389')
postdriver.switch_to.active_element.type('Tab')
postdriver.find_element_by_pro('bWpxjgudeyUVu7V').type('Payal@209')    
postdriver.switch_to.active_element.type('Enter') 



from flask import Flask, request, jsonify
app = Flask(__name__)
def searchAll(search,peoplekeyword):
    print("search start for")
    print(search)
    print("search end for")    

    url = "https://www.linkedin.com/jobs/search/?keywords="+str(search) 
    driverkeyword.get(url)
    
    src = driverkeyword.find_element_by_class_name('jobs-search__results-list').get_attribute('innerHTML')

    soup = BeautifulSoup(src, 'html.parser')
    
    jobs = []
    for li in soup.find_all('li',limit= 5  ):
       
        imgsrc =  li.find( 'img' , {'class': 'artdeco-entity-image'})
        time_tag =  li.find('time', {'class': 'job-search-card__listdate'})
        if time_tag is not None:
           time_tag =  li.find('time', {'class': 'job-search-card__listdate'})
        else:          
            time_tag =  li.find('time', {'class': 'job-search-card__listdate--new'})
        
        parsed_url = urlparse( li.find('a', {'class': 'base-card__full-link'}).get('href')  )
        query_dict = parse_qs(parsed_url.query)    
        job = {           
        'jobtitle': li.find('h3', {'class': 'base-search-card__title'}).text.strip(),
        'cname': li.find( 'a' , {'class': 'hidden-nested-link'}).text.strip(),
        'clogo':  imgsrc.get('src')  , 
        'location':  li.find('span', {'class': 'job-search-card__location'}).text.strip(), 
        'time':  time_tag.text.strip(), 
         'link': parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path
        }
        jobs.append(job)
        for obj in jobs:
            driver.get(obj['link'])             
            element = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.CLASS_NAME, "jobs-unified-top-card"))
            )            
            jobsrc  = driver.find_element_by_class_name('jobs-unified-top-card').get_attribute('innerHTML')                      
            jobsoup = BeautifulSoup(jobsrc, 'html.parser')

            aboutjobsrc  = driver.find_element_by_class_name('jobs-description__content').get_attribute('innerHTML')                      
            aboutjobsoup = BeautifulSoup(aboutjobsrc, 'html.parser')   
            obj['companylink']  = jobsoup.find_all('a')[0].get("href")
            obj['aboutjob']  = aboutjobsoup.find_all('span')[0].getText()
            ul_elements = jobsoup.find_all('ul')
            li_texts = []
            for ul in ul_elements:
             li_elements = ul.find_all('li')
             for li in li_elements:
               li_texts.append(li.get_text())            
            obj['cinfo']  = li_texts 
            obj['companylink'] = "https://www.linkedin.com"+obj['companylink'].replace('/life', '')
            obj['companyabout'] =   obj['companylink']+"about"
            obj['companyceo'] =    obj['companylink']+"people/?keywords="+str(peoplekeyword)
          
            driver.get(obj['companyabout']) 
            
            element = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.CLASS_NAME, "application-outlet"))
            ) 
            aboutsrc  = driver.find_element_by_class_name('application-outlet').get_attribute('innerHTML')   
            aboutsoup = BeautifulSoup(aboutsrc, 'html.parser')   
            srcfile =  aboutsoup.find('section', {'class': 'artdeco-card p5 artdeco-card mb4'})

            pelement = WebDriverWait(driver, 10).until(
                      EC.presence_of_element_located((By.TAG_NAME, "p"))
            ) 
            first_inner_p = srcfile 
            if first_inner_p is not None:
              obj['aboutcompany'] = first_inner_p.find("p").getText()
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

          
            driver.get(obj['companyceo']) 
            time.sleep(20)
            WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CLASS_NAME, "scaffold-layout--main-aside"))
             )    
          
           
            data = driver.find_element_by_class_name('scaffold-layout--main-aside').get_attribute('innerHTML')  
            ceosoup = BeautifulSoup(data, 'html.parser')

             
            ceobox =  ceosoup.find('div', {'class': 'scaffold-finite-scroll--infinite'})
         
            if ceobox is not None:
                ceos = []
                for li in ceobox.find_all('li'):
                 info = { }      
                 people = li.find( class_ = "org-people-profile-card__profile-title" ) 
                 peoplesubtitle = li.find( class_ = "artdeco-entity-lockup__subtitle" ) 
                 
                 if people is not None:
                        info['name'] = people.text.strip()
                 else:
                        info['name'] = "No Data Found"  

                 if peoplesubtitle is not None:
                        info['subtitle'] = peoplesubtitle.text.strip()
                 else:
                        info['subtitle'] = "No Data Found"         
                 info['phone'] = "XXXXXXXXXXXXX"
                 info['email'] = "XXXXXXXXXXXXX"

                 linkedlink = li.find( class_ = "app-aware-link" ) 
                 if linkedlink is not None:
                        info['link'] = linkedlink.get('href') 
                 else:
                        info['link'] = "No Data Found"  
                            
                ceos.append(info)
                obj['peoples'] = ceos
            else:
                obj['peoples'] = []    

            print(f"data is ready for  {obj['cname']}")
            sio.emit('identity',  obj )
            
    return jobs
def searcPost(search):
    print('request start number', search )
    url = "https://www.linkedin.com/search/results/content/?keywords=looking for "+str(search)     
    postdriver.get(url)
    time.sleep(20)
    src = postdriver.find_element_by_class_name('scaffold-finite-scroll__content').get_attribute('innerHTML')
   
 
    soup = BeautifulSoup(src, 'html.parser')    
    posts = []
    for li in soup.find_all('li' ):    
     
        com = li.find('div', {'class': 'update-components-text'}); 
        if com is not None:
       
         userlink = li.find('a', {'class': 'app-aware-link'}).get('href') 
         usercomment = li.find('div', { 'class' : 'update-components-text' }).text.strip()       
         timeago =  li.find('div', { 'class' : 'update-components-text-view' }).text.strip()  
         emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", usercomment)
         phones =  re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', usercomment)
         userpost = {        
           'email': emails ,
           'phone' :   phones,
           'usercomment': usercomment ,
           'timeago' : timeago
         }
 
      
         
         postdriver.get(userlink)
         time.sleep(5)
         peoplesrc = postdriver.find_element_by_class_name('pv-top-card').get_attribute('innerHTML')
         peoplesoup = BeautifulSoup(peoplesrc, 'html.parser')  


         if  li.find('div', {'class': 'update-components-text'}) is not None:
               userpost['comment' ] = li.find('div', {'class': 'update-components-text'}).text.strip()
         else:
               userpost['comment' ] = ""

         if  userlink is not None:
               userpost['link' ] = userlink
         else:
               userpost['link' ] = ""   

         if  peoplesoup.find('h1', {'class': 'text-heading-xlarge'})  is not None:
               userpost['name' ] = peoplesoup.find('h1', {'class': 'text-heading-xlarge'}).text.strip()
         else:
               userpost['name' ] = ""                        

         if  peoplesoup.find('div', {'class': 'text-body-medium'})  is not None:
               userpost['subtitle' ] = peoplesoup.find('div', {'class': 'text-body-medium'}).text.strip()
         else:
               userpost['subtitle' ] = ""  

         if  peoplesoup.find('span', {'class': 'pv-text-details__right-panel-item-text'}) is not None:
               userpost['company' ] = peoplesoup.find('span', {'class': 'pv-text-details__right-panel-item-text'}).text.strip() 
         else:
               userpost['company' ] = ""  

         if   peoplesoup.find(class_='pv-text-details__left-panel mt2')   is not None:
               userpost['location' ] =  peoplesoup.find(class_='pv-text-details__left-panel mt2').text.strip() 
         else:
               userpost['location' ] = ""           
         sio.emit('identity',  userpost )
 
         posts.append(userpost)        
    return posts

@app.route('/', methods=['GET'])  
def foo():
    print('request start======================================')
    search = request.args.get("keyword")     
    peoplekeyword = request.args.get("people")  
    for data in search.split(","):
     print("=====")
#      print(data)
#      print(peoplekeyword)
#      print("=====")
#      searchAll(data,peoplekeyword) 
    return "ok"

@app.route('/mainbox', methods=['GET'])  
def mainbox():
    search = [];    
    search = request.args.get("keyword").split(",")
    for s in search:
      time.sleep(10)
      print("start search for " , search)
      searcPost(s)
    return "ok"
 
if __name__ == '__main__':
 app.run(debug=False, port=8001)