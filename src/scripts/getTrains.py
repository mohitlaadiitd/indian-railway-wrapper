import requests
from bs4 import BeautifulSoup
import csv
import selenium
from selenium import webdriver
import json

# get the html content
def get_html(url):
    # get the html content using driver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html

# check if style of the row is display: none
def visible(tr):
    style = tr.get('style')
    if style and style == 'display: none;':
        return False
    return True

# get the data from the html content
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # # get all the rows of the table that has attribute of data-train (all the rows)
    trs = soup.find_all('tr', attrs={'data-train': True})
    trains = []
    for tr in trs:
        if visible(tr):
            # write the data to a csv file
            data_train = json.loads(tr.get('data-train'))
            data = {
                'num': data_train.get('num'),
                'name': data_train.get('name'),
                'from': data_train.get('s'),
                'to': data_train.get('d'),
                'from_time': data_train.get('st'),
                'to_time': data_train.get('dt'),
                'duration': data_train.get('tt')
            }
            trains.append(data)
            # write_csv(data)
    return trains

# write the data to a csv file
def write_csv(data):
    with open('trains.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['num'], data['name'], data['from'], data['to'], data['from_time'], data['to_time'], data['duration']))

def getTrains(source, destination, date):
    url = f'https://etrain.info/trains/{source}-to-{destination}?date={date}'
    return get_data(get_html(url))

if __name__ == '__main__':
    getTrains()()