# scrap data from https://www.cleartrip.com/trains/stations/list?page=1 
# and save it to a csv file

import requests
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
from lxml import etree
import json
import time 

# get the html content
def get_html(url):
    r = requests.get(url)
    return r.text

# get the data from the html content
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # find table with class 'wikitable sortable'
    trs = soup.find('table', class_='wikitable').find_all('tr')
    for tr in trs[1:]:
        td = tr.find_all('td')[0]
        data = {
            # get the text between the > and < tags
            'station': td.text.split('>')
        }
        write_csv(data)

# write the data to a csv file
def write_csv(data):
    with open('junctions.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['station']))

def main():
    url = 'https://en.wikipedia.org/wiki/List_of_railway_junction_stations_in_India'
    get_data(get_html(url))
    # delete all the lines in the csv file that have " as the value
    with open('junctions.csv', 'r') as f:
        lines = f.readlines()
    with open('junctions.csv', 'w') as f:
        for line in lines:
            if line.strip("\n") != '"':
                if line[0] == '"' or line[0] == ' ': f.write(line[1:])
                else: f.write(line)

if __name__ == '__main__':
    main()