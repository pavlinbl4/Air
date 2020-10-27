import requests
from bs4 import BeautifulSoup

URL = 'https://newprospect.ru'
# URL = 'https://www.tassphoto.com/ru/asset/fullTextSearch/search/%D1%81%D0%B5%D0%BC%D0%B5%D0%BD+%D0%BB%D0%B8%D1%85%D0%BE%D0%B4%D0%B5%D0%B5%D0%B2/page/1'
HEADERS = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4200.0 Iron Safari/537.36","accept" : "*/*"}

def get_html(url,params = None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,"html.parser")
    # items = soup.find_all('div',class_='cs-entry__excerpt') # New prospect работает
    items = soup.find_all('h6', class_='cs-entry__title')
    # items = soup.find_all('p', 'result-counter') # версия для TASS
    images = []
    for item in items:

        images.append({
           'title': item.find('h6', class_='cs-entry__title')
        })
    print(items)
    print(images)

def parse():
    html = get_html(URL)
    # print(html.status_code)
    if html.status_code == 200:
        # print(html.text)
        get_content(html.text)

    else:
        print("error")

parse()