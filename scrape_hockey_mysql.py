# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:44:53 2026

@author: anuar
"""

import requests
from bs4 import BeautifulSoup
import time
import mysql.connector

# establishing connection
conn = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = input('Enter Mysql password: ')
    database = 'countries'
    )
# CREATING CURSOR FOR WRING INSIDE THE DB
cursor = conn.cursor()
 # creating Table

#cursor.execute(
'''CREATE TABLE TEAM_SCORE(
    Team_name VARCHAR(100) PRIMARY KEY,
    Year INT,
    wins INT,
    losses INT,
    ot_losses INT,
    win_percent INT,
    goal_for INT,
    goal_against INT,
    point_win_loss INT)'''

for page in range(1,11):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={page}'

    html_file = requests.get(url)
    soup = BeautifulSoup(html_file.text,'lxml')
    # scrap html tags
    teams = soup.find_all('tr',class_ = 'team')
    # iterate over list of tags
    for team in teams:
        name = team.find('td',class_='name').text.strip()
        year = team.find('td',class_='year').text.strip()
        wins = team.find('td',class_='wins').text.strip()
        losses = team.find('td',class_='losses').text.strip()
        ot_losses_raw = team.find('td',class_='ot-losses').text.strip()
        if ot_losses_raw == '' or ot_losses_raw is None:
            ot_losses = 0
        else:
            ot_losses = int(ot_losses_raw)
        win_percent = team.find('td',class_='pct text-success')
        if win_percent is not None:
            win_percent = team.find('td',class_='pct text-success').text.strip()
        else:
            None
        goal_for = team.find('td',class_='gf').text.strip()
        goal_against = team.find('td',class_='ga').text.strip()
        point_win_loss = team.find('td',class_='diff text-succes')
        if point_win_loss is not None:
            point_win_loss = team.find('td',class_='diff text-succes').text.strip()
        else:
            None
        cursor.execute('''INSERT INTO TEAM_SCORE(
            Team_name,year,wins,losses,ot_losses,
            win_percent,goal_for,goal_against,point_win_loss)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(name,year,wins,losses,ot_losses,
        win_percent,goal_for,goal_against,point_win_loss))
conn.commit()
conn.close()      
            
time.sleep(1)