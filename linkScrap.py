# This scrpt will pull the download links 
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
    href = link.get('href') 

    # modifying relative download links to absolute links
    dl_link = 'https://talkpython.fm/episodes/download' + href[14:] + '.mp3\n'
    file.write(dl_link.encode())
file.close()
print('Saved')

