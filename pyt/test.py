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


 


from flask import Flask, request, jsonify
app = Flask(__name__)
 
def searcPost(search):
  print(search)

@app.route('/mainbox', methods=['GET'])  
def mainbox():
    search = [];    
    search = request.args.get("keyword").split(",")
    for s in search:
      time.sleep(2)
      print("start search for " , search)
      searcPost(s)
    return "ok"
 
if __name__ == '__main__':
 app.run(debug=False, port=8001)