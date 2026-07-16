# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 10:27:51 2026

@author: anuar
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

classification = open('turtle.csv','w',newline='',encoding='utf-8')
# creating csv writer
writer = csv.writer(classification)
# creating the heading
writer.writerow(['family name','more info'])
# control browser. AUTOMATION AND CONTROL FROM EXIT BEFORE COMPLETE LOADING
option = Options()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options = option)
# provide url to driver
url = 'https://www.scrapethissite.com/pages/frames/'
driver.get(url)
# find frame / iframe
all_iframe = driver.find_elements(By.TAG_NAME,'iframe')
# dive to the frame 
driver.switch_to.frame(all_iframe[0])
# grab the html of iframe
html_file = driver.page_source
# find body tag inside the frame
driver.switch_to.default_content()

soup = BeautifulSoup(html_file,'lxml')
value = soup.find_all('div',class_='col-md-4 turtle-family-card')
for values in value:
    image = values.img.get('src')
    family = values.h3.text.strip()
    learn_more = values.a['href']
    
    writer.writerow([family,learn_more])


time.sleep(3)
driver.quit()

classification.close()