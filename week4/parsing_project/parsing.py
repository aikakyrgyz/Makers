from datetime import datetime 
from multiprocessing import Pool
import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"} #to avoid 403 code
    response = requests.get(url, headers = headers)
    # print(response.status_code)
    return response.text #returns all of the html content of the site

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml') #creates a soup object
    pages_ul = soup.find('div', class_ = "qkT05Iu").find('ul') #returns the content of the div tag with the specified class
    last_page = pages_ul.find_all('li')[-2] 
    total_pages  = last_page.find('a').get('href').split('=')[-1]
    return int(total_pages)

    #pages_a= pages_ul.find_all('li') #return a list of all the li tags
    # pages_a[-1] returns second to last page:
    # <li class="next"><a aria-disabled="false" aria-label="Next page" href="/c/noutbuki/?page=2" role="button" tabindex="0"><span class="_3Z2A4XT _3CF5OcL"></span></a></li>
    # print(soup.prettify())
    # total_pages = last_page.find('a').get('href') #returns: "/c/noutbuki/?page=35"

def write_to_csv(data):
    with open('laptops.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter = '|')
        writer.writerow((data['title'],
                         data['price'],
                         data['image']
                        ))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_="_2UG66IO").find('ul', class_="_1h4EpkX") #accesing only the products of the page 
    products = product_list.find_all('li', class_="_3uUsGGA") #list of products
    for product in products:
        #image, title, price
        try:
            image = product.find('div', class_="AkWZIIC").find('a').find('img').get('src')
        except:
            image = ''
        try:
            title = product.find('div', class_= "_2fFxlhy").find('a').text
        except:
            title = ''
        try:
            price = product.find('div', class_ = "_3Fsz1sA").find('span').text
        except:
            price =''
        all_data = {'title': title, 'price': price, 'image':image}
        write_to_csv(all_data)

def speed_up(url):
    html = get_html(url)
    data = get_page_data(html)



def main():
    start = datetime.now()
    site_url = 'https://www.eldorado.ru/c/noutbuki/'
    pages = '?page='
    total_pages = get_total_pages(get_html(site_url))
    urls = [site_url + pages + str(page) for page in range(1, total_pages+1)]
    with Pool(40) as p:
        p.map(speed_up, urls) 
    print(total_pages)
    # for page in range(1, total_pages+1):
    #     url_page = site_url + pages + str(page) #url of each page
    #     html = get_html(url_page) #html info of whole page
    #     get_page_data(html) #getting the data from the html 
    end = datetime.now()
    print('Time: ', end - start)

if __name__ == '__main__':
    main()