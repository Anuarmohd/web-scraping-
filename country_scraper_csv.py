# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# TO SCRAP AND SAVE DATA IN CSV FILE
from bs4 import BeautifulSoup
import requests
import csv
url = 'https://www.scrapethissite.com/pages/simple/'
# openind the file named countries
csv_file = open('countries.csv','w')
#creating writer object that know how to formart data in file
csv_writer = csv.writer(csv_file)
# writing column header
csv_writer.writerow(['Country Name','Capital City','Population','Area in km2'])

html_file = requests.get(url)
soup = BeautifulSoup(html_file.text,'lxml')

country = soup.find_all('div',class_= 'col-md-4 country')

# iterate to get an individual countries

for countries in country:
    country_name = countries.h3.text.strip()
    capital_city = countries.find('span',class_ = 'country-capital').text.strip()
    population = countries.find('span',class_ = 'country-population').text.strip()
    Area_km2 = countries.find('span', class_ ='country-area').text.strip()   
      # insert the data to file using writer       
    csv_writer.writerow([country_name,capital_city,population,Area_km2])
csv_file.close()    
