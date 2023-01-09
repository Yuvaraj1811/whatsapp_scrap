
from flask import Flask,render_template,request,session, abort,send_file,send_from_directory,redirect,url_for,make_response
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from datetime import datetime
import schedule
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from unidecode import unidecode
import pandas as pd
options = Options()
import re
# import pymssql
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import configparser
from multiprocessing import Process
from threading import Thread
import uuid
import urllib.request
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="scrapping_practice"
)
app = Flask(__name__)
app.secret_key = 'yuvaraj2412' 

@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        driver=webdriver.Chrome(r"C:\\Users\Admin\Desktop\\Yuvaraj\Scrapping\\chromedriver.exe")
        driver.get("https://web.whatsapp.com/")
        driver.maximize_window()
        time.sleep(3)

        import schedule
        def qr_img():
            # driver.save_screenshot('screenshot.png'.format(i))
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div").click()
                print("Clicking reload")
            except:
                print("No reload found")
            time.sleep(3)
            qr_code=driver.find_element_by_class_name("_2UwZ_")
            save_name = 'qr_img_{}.jpg'.format(str(datetime.now().strftime('%d-%m-%Y , %H-%M-%S')))
            
            # qr_code.screenshot(r'C:\\Users\Admin\Desktop\\try/{}'.format(save_name))
            qr_code.screenshot(r'C:\\Users\Admin\Desktop\\Yuvaraj\\Python_flask\whatsapp_qr\static\\files/{}'.format(save_name))

            # time.sleep(22)
        schedule.every(18).seconds.do(qr_img)

        while True:  
            
            schedule.run_pending()
    return render_template("index.php",qr_code=qr_code)

    
if __name__ == '__main__':
   app.run(debug=True,port=8002)
    
    
    
   


    
    
    

