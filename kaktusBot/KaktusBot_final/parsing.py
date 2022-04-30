from multiprocessing import Pool
import csv
import json
import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"} 
    response = requests.get(url, headers = headers)
    return response.text 
def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup
def get_link_data(html):
    soup = get_soup(html)
    description = ''
    block = soup.find('div', class_="BbCode").find_all('p')
    for p in block:
        description +=p.text
    return description

def write_to_csv(data, choice):
    if choice == 'today':
        with open('today.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter = '|')
            writer.writerow((data['index'],
                            data['title'],
                            data['image'],
                            data['link'],
                            data['description']
                            ))
    else:
        with open('yesterday.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter = '|')
            writer.writerow((data['index'],
                            data['title'],
                            data['image'],
                            data['link'],
                            data['description']
                            ))       


def get_page_data(html):
    soup_main = get_soup(html)
    vse_novosti_page_url = soup_main.find('a', class_="Main--all_news-link").get('href') #today link
    soup_today = get_soup(get_html(vse_novosti_page_url))
    vse_novosti_page_url_yesterday = soup_today.find('a', class_="PaginatorDate--yesterday").get('href') #yesterday link
    soup_yesterday = get_soup(get_html(vse_novosti_page_url_yesterday))
    articles = soup_today.find('div', class_="Tag--articles").find_all('div', class_="Tag--article")
    articles_yesterday = soup_yesterday.find('div', class_="Tag--articles").find_all('div', class_="Tag--article")
    index=0
    for article in articles:
        index = index+1
        title = article.find('a', class_="ArticleItem--name").text
        link = article.find('a', class_="ArticleItem--image").get('href')
        image = article.find('img', 'ArticleItem--image-img').get('src')
        description = get_link_data(get_html(link))
        all_data = {'index': index, 'title': title, 'image': image, 'link':link, 'description': description}
        write_to_csv(all_data, 'today')
    index = 0
    for article in articles_yesterday:
        index = index+1
        title = article.find('a', class_="ArticleItem--name").text
        link = article.find('a', class_="ArticleItem--image").get('href')
        image = article.find('img', 'ArticleItem--image-img').get('src')
        description = get_link_data(get_html(link))
        all_data = {'index': index, 'title': title, 'image': image, 'link':link, 'description': description}
        write_to_csv(all_data, 'yesterday')
def clear():
    f = open('yesterday.csv', "w+")
    f.write('')
    f.close()
    f2 = open('today.csv', 'w+')
    f2.write('')
    f2.close()


def main():
    site_url = 'https://kaktus.media/'
    get_page_data(get_html(site_url))
# main()