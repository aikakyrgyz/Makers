import csv

from bs4 import BeautifulSoup
import requests

all_data = {}
def get_html(url):
     headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"} #to avoid 403 code
     response = requests.get(url, headers = headers)
     return response.text
def write_to_csv(data):
    with open('valuta.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter = '|')
        writer.writerow((data['currency'], data['index']))
def get_site_data(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_="col-md-8")
    course_table = table.find('table', class_="kurs-table")
    course_names = course_table.find_all('tr')[1:]
    rate_table = table.find('div', class_="kurs-bar__item").find_all('tr')
    print(rate_table)
    for tr in course_names:
        currency = tr.find('div').text
        all_data = {'currency':currency, 'index':0}
        write_to_csv(all_data)
        

def main():
    URL = 'https://valuta.kg'
    get_site_data(get_html(URL))

main()
