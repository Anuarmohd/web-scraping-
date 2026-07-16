# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:02:13 2026

@author: anuar
"""
# SCRAPE USING REQUEST LINK FOR JAVASCRIPT WEBSITE WITH RESULT IN LINK IN REQUEST


import requests
import csv

# open and create file\
csv_file = open('my_movies.csv','w')
#create a writer
csv_writer = csv.writer(csv_file)
# writing the heading of the file valus
csv_writer.writerow(['movie title','year','Award','Nomination'])

for years in range(2010,2016):
    url = f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year={years}'
    movies = requests.get(url).json()
    
    for movie in movies:
        title = movie['title']
        year = movie['year']
        award = movie['awards']
        nomination = movie['nominations']
        
        csv_writer.writerow([title,year,award,nomination])
csv_file.close()