import requests
from bs4 import BeautifulSoup
import re

url = 'https://talkpython.fm/episodes/all'      # webpage to scrap
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, "lxml")
links = soup.find_all('a' , href=re.compile('episodes/show'))   # finds links with 'episodes/show' in it's url

# writing to file 

file = open("data.txt", 'wb')
print('Collecting the links...')
for link in links:
    href = link.get('href') + '\n'
    file.write(href.encode())
file.close()
print('Saved')