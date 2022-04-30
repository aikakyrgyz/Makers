# import requests
# from bs4 import BeautifulSoup as bs



# def get_html(url):
#     response = requests.get(url)
#     return response.text    

# def main():
#     site_url = 'http://kenesh.kg/ru/deputy/list/35'
#     html = get_html(site_url)
#     deputy_links = get_depputy_links(html)
#     print(deputy_links)
#     deputy_list = []
#     for link in deputy_links:
#         data = get_data(get_html('hhtp://kenesh.kg'+ link))
#         deputy_list.append(data)
#     # print(deputy_list, end = '\n')
# def get_depputy_links(html):
#     soup = bs(html, 'lxml')
#     all_data = soup.find('div', class_="col-xs-12").find('table', class_ = 'table').find('tbody').find_all('td')
#     deputy_link = set()
#     for td in all_data:
#         link = td.find('a').get('href')
#         if link.startswith('/ru/deputy/show'):
#             deputy_link.add(link)
#     return deputy_link
# def get_data(html):
#     soup = bs(html, 'lxml')
#     description= soup.find('div', class_="deputy-contacts")
#     name = description.find('h3', class_="font-bold mb-10 deputy-name").text.strip()
#     commitet_fraction = description.find_all('h4')
#     commitet_fraction = list(map(lambda tag: tag.text.strip(), commitet_fraction))
#     commitet, fraction = commitet_fraction
#     try:
#         tel = description.find('p',class_="font-bold mb-10").find('a').text.strip()
#     except:
#         tel = ''
#     return(name, commitet, fraction, tel)

    
# if __name__ == '__main__':
#     main()

import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    response = requests.get(url)
    return response.text

def get_deputy_links(html):
    soup = bs(html, 'lxml')
    all_data = soup.find('div', class_='col-xs-9').find(
                         'table', class_='table').find(
                         'tbody').find_all('td')
    deputy_links = set()
    for td in all_data:
        link = td.find('a').get('href')
        if link.startswith('/ru/deputy/show/'):
            deputy_links.add(link)
    return deputy_links

def get_data(html):
    soup = bs(html, 'lxml')
    description = soup.find('div', class_='deputy-contacts')
    name = description.find('h3', class_='deputy-name').text.strip()
    commitet_fraction = description.find_all('h4')
    commitet_fraction = list(map(lambda tag: tag.text.strip(),
                             commitet_fraction))
    fraction, commitet = commitet_fraction
    try:
        tel = description.find('p', class_='font-bold mb-10').find(
                               'a').text.strip()
    except:
        tel = ''
    return (name, fraction, commitet, tel)


def main():
    site_url = 'http://kenesh.kg/ru/deputy/list/35'
    html = get_html(site_url)
    deputy_links = get_deputy_links(html)
    deputy_list = []
    for link in list(deputy_links):
        data = get_data(get_html('http://kenesh.kg' + link))
        deputy_list.append(data)
    print(deputy_list)
    return deputy_list

if __name__ == '__main__':
    main()


