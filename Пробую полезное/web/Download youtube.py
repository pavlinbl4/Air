url = 'https://youtu.be/ivcLKQj1i1I'
video_name = url.split('/') [-1]

# using requests

# imported the requests library
import requests

print
"Downloading file:%s" % video_name

# download the url contents in binary format
r = requests.get(url)

# open method to open a file on your system and write the contents
with open('tutorial.mp4', 'wb') as f:
    f.write(r.content)

# using urllib

# imported the urllib library
import urllib.request

print
"Downloading file:%s" % video_name

# Copy a network object to a local file
urllib.request.urlretrieve(url, "tutorial2.mp4")