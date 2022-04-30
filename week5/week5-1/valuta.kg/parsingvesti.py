import csv

import requests
from bs4 import BeautifulSoup


all_data ={}
def get_html(URL):
  headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
  response = requests.get(URL, headers = headers)
  return response.text

def write_to_csv(data):
  with open('vesti.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter ='|')
    writer.writerow((data['index'], data['title']))


def get_page_data(html):
  index = 0

  soup = BeautifulSoup(html, 'lxml')

  news_block = soup.find('div', class_= "itemList").find_all('div', class_="itemContainer itemContainerLast")
 
  for i in news_block:
    index = index+1
    title = news.find('div', class_="itemImageBlock").find('a').get('title')
    all_data = {'index':index, 'title':title}
    write_to_csv(all_data)
  

  # news_block = soup.find('div', class_="itemListView").find_all('div', class_="itemBlock")
  # for news in news_block:
  #   title = news.find('div', class_="itemIntroText").find('p').text
  #   print(title)

def main():
  URL = 'https://vesti.kg'
  # html = get_html(url)
  # get_page_data(html)
  


  get_page_data(get_html(URL))

main()

