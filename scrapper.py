# scrap data from https://www.cleartrip.com/trains/stations/list?page=1 
# and save it to a csv file

import requests
from bs4 import BeautifulSoup
import csv

# get the html content
def get_html(url):
    r = requests.get(url)
    return r.text

# get the data from the html content
def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table').find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        data = {
            'code': tds[0].text.strip(),
            'name': tds[1].text.strip(),
            'location': tds[2].text.strip(),
            'density': int(tds[3].text.strip()) if tds[3].text.strip() != '' else 0
        }
        write_csv(data)

# write the data to a csv file
def write_csv(data):
    with open('stations.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['code'], data['name'], data['location'], data['density']))

def main():
    url = 'https://www.cleartrip.com/trains/stations/list?page='
    for i in range(1, 6):
        get_data(get_html(url + str(i)))

if __name__ == '__main__':
    main()