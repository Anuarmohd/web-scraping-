# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 07:55:05 2026

@author: anuar
"""
import csv
import requests
from bs4 import BeautifulSoup
import time

#opening the file and named match analysis
csv_file = open('match analysis.csv','w')
# create a write for writing in the file
csv_writer = csv.writer(csv_file)
# writing the hear for the file
csv_writer.writerow(['Team Name','Year','Wins',
                     'Losses','OT Losses','Win %',
                     'Goal For (GF)','Goals Against (GA)','Point losses/Gain'])


for page in range(1,25):
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
        ot_losses = team.find('td',class_='ot-losses').text.strip()
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
        csv_writer.writerow([name,year,wins,losses,ot_losses,win_percent
                             ,goal_for,goal_against,point_win_loss])
time.sleep(1)
