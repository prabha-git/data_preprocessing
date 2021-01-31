import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/2015_in_hip_hop_music'

page = requests.get(url)

#print(page.content)
soup = BeautifulSoup(page.content,'html.parser')

results = soup.find_all('table',class_='wikitable')[1]

for record in soup.find_all('tr'):
    albumdata=""
    for data in record.find_all('td'):
        albumdata = albu,data+","+