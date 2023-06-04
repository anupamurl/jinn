from flask import Flask, request
from bs4 import BeautifulSoup
import time
from selenium_pro import webdriver
from selenium_pro.webdriver.support.ui import WebDriverWait
from selenium_pro.webdriver.support import expected_conditions as EC
from selenium_pro.webdriver.common.by import By

driver = webdriver.Start()

app = Flask(__name__)

@app.route('/',  methods=['GET'])
def hello_world():
    search = request.args.get("keyword")
    print('request start')
    url = "https://www.google.com/maps/search/"+str(search)    
    driver.get(url)
    time.sleep(20)
    src = driver.find_element_by_tag_name('body').get_attribute('innerHTML')
    data =   src.selectAll('[role="article"]')
    for d in data:
     print('request start number',  d)
    return src
app.run(debug=True, port=8002)

 