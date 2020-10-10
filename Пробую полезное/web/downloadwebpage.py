

from urllib.request import urlopen
html = urlopen("https://www.skoda-avto.ru/models/karoq2020").read().decode('utf-8')
print(html)
