import requests
import json

def get_html(url):
    response = requests.get(url, headers = {'User-agent':'your bot:01'})
    python_object = json.loads(response.text)
    news = python_object['data']['children']
    returned_news =[]
    number = 0
    for new in news:
        number+=1
        new_dict = {
            f'News No. {number}': 
                {
                'title':new['data']['title'],
                'created':new['data']['created'],
                'author':new['data']['author']
                }
                }
        returned_news.append(new_dict)
    return returned_news
def write_to_json(data):
    with open('redditnews.json', 'w') as my_file:
        json.dump(data, my_file, indent = 5)


def main(url):
    data = get_html(url)
    write_to_json(data)
main('https://www.reddit.com/.json')
