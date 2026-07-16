# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:28:44 2026

@author: anuar
"""
import requests
from bs4 import BeautifulSoup

# This is our FAKE envelope (Spoofed Headers)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
url = 'https://www.scrapethissite.com/pages/advanced/?gotcha=headers'

response = requests.get(url, headers = headers)

print(response.status_code)

soup = BeautifulSoup(response.text,'lxml')

print(soup)