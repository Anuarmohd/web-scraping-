# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:36:51 2026

@author: anuar
"""
# SCRAPE AND IMPORT TO MYSQL DB 
from bs4 import BeautifulSoup
import requests
import mysql.connector

url = 'https://www.scrapethissite.com/pages/simple/'
html_file = requests.get(url)
soup = BeautifulSoup(html_file.text,'lxml')
# CONNECT TO MYSQL SERVER
conn = mysql.connector.connect(
 host ='127.0.0.1',
 user = 'root',
 password = input('enter Mysql password: ')
 database = 'countries'
 )
cursor = conn.cursor()
#CREATING TABLE TO DB

#cursor.execute('''CREATE TABLE COUNTRY_DETAILS
'''               (id INT PRIMARY KEY AUTO_INCREMENT,
                country_name VARCHAR(100),
                capital_city VARCHAR(100),
                population INT,
                Area INT)'''



country = soup.find_all('div',class_= 'col-md-4 country')

# iterate to get an individual countries

for countries in country:
    country_name = countries.h3.text.strip()
    capital_city = countries.find('span',class_ = 'country-capital').text.strip()
    population_raw = countries.find('span',class_ = 'country-population').text.strip()
    Area_km2_raw = countries.find('span', class_ ='country-area').text.strip() 
    population = int(population_raw.replace(',',''))
    Area = float(Area_km2_raw.replace(',',''))
    cursor.execute(''' INSERT INTO COUNTRY_DETAILS
                   (country_name,capital_city,population,Area)
                   VALUES(%s,%s,%s,%s)''',(country_name,capital_city,population,Area))
conn.commit()
conn.close()    
    
    
    
    
    
    
    
    
    
