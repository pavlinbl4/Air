"""
Проверяет ТАСС фото и сохраняет данные о количестве снимков на данную дату в файл

"""
import requests
from bs4 import BeautifulSoup

URL = 'https://www.tassphoto.com/ru/asset/fullTextSearch/search/%D1%81%D0%B5%D0%BC%D0%B5%D0%BD+%D0%BB%D0%B8%D1%85%D0%BE%D0%B4%D0%B5%D0%B5%D0%B2/page/1'
HEADERS = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4200.0 Iron Safari/537.36","accept" : "*/*"}

def get_html(url,params = None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    from datetime import date
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all('p', 'result-counter')
    items = str(items)
    print(date.today(),"  всего снимков -",items[42:47])
    n = open('Tass information.txt', 'a')
    date = str(date.today())
    n.write(date)
    n.write("  всего снимков - ")
    n.write(items[42:47]+'\n')
    n.close()

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)

    else:
        print("error")

parse()




