# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:52:48 2026

@author: anuar
"""
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/advanced/?gotcha=login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.scrapethissite.com/pages/advanced/?gotcha=login',  # <--- ADD THIS LINE
}
session = requests.session()
data = {'username':'admin','password':'admin'}
# spoofing header
first_response = session.get(url,headers = headers)
#response = session.post(url,data)


soup = BeautifulSoup(first_response.text,'lxml')
#token = soup.find('input')
# WE SEND LOGIN CREDENTIAL TO A SET TO GIVE COOKIES
