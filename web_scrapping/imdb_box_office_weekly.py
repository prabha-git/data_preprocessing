import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'

page = requests.get(url)


soup = BeautifulSoup(page.content,'html.parser')

table = soup.find(id='thetable').find('tbody')

rows = table.find_all('tr')

country = []
cases=[]
deaths=[]
recovered=[]

for row in rows:
    if len(row)== 12:
        cells = row.find_all('td')
        
        if len(cells)>0:
            header = row.find_all('th')[1]
            country.append(header.text.strip())
            cases.append(cells[0].text.strip().replace(',',''))
            deaths.append(cells[1].text.strip().replace(',',''))
            recovered.append(cells[2].text.strip().replace(',',''))
            
df = pd.DataFrame({"country":country,"cases":cases,"deaths":deaths,"recovered":recovered})
print(df)
    