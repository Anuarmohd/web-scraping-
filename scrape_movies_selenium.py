# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:59:50 2026

@author: anuar
"""

# SCRAPE JAVASCRIPT USING SELENIUM
# import the driver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import csv

movie_file = open('movies_award.csv','w',newline='',encoding='utf-8')
writer = csv.writer(movie_file)
writer.writerow(['title','nomination','award'])
# CONTROL THE BROWSER AUTOMATICALLY AND STABILIZING FROM CLOSING PREMATURELY
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

# TELL BROWSER TO LOAD SITE BY GIVING URL

url = 'https://www.scrapethissite.com/pages/ajax-javascript/'
driver.get(url)


print(f'scrape data for year :2010')
#wait up to 10 sec for target year button to be visible and find the button to be clicked
button_year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,f'2010')))
# clicking the button simulation it
button_year.click()
# wait before take snapshot
time.sleep(10)

# take snapshot of fully html code
html_file_snap = driver.page_source
driver.quit()
soup = BeautifulSoup(html_file_snap,'lxml')

movies = soup.find_all('tr',class_='film')
# iterate on list of data
for movie in movies:
    title = movie.find('td',class_='film-title').text.strip()
    nomination = movie.find('td',class_='film-nominations').text.strip()
    award = movie.find('td',class_= 'film-awards').text.strip()
    
    writer.writerow([title,nomination,award])
driver.quit()

movie_file.close()
    
    




