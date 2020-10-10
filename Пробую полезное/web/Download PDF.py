url = 'https://www.skoda-avto.ru/m/pricelists'

# downloading with urllib.request

# import the urllib package
import urllib.request

# Copy a network object to a local file
urllib.request.urlretrieve(url, "karoq-price.pdf")

# downloading with requests

# import the requests library
import requests

# download the file contents in binary format
r = requests.get(url)

# open method to open a file on your system and write the contents
with open("karoq-price.pdf", "wb") as code:
    code.write(r.content)