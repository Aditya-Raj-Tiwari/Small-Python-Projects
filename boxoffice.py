from bs4 import BeautifulSoup
import requests

requestObj = requests.get('https://www.boxofficemojo.com/')
soup = BeautifulSoup(requestObj.text,'html.parser')

list = soup.find_all("div", class_ = "hp_boteaser")


regions = soup.find_all('div', {'class': 'hp_boteaser'})
for region in regions:
    table = region.find('table', {'id': 'hp_boxoffice'})
print(table.text)