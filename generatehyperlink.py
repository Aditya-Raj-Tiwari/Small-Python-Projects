from bs4 import BeautifulSoup
import requests

f = open('GeratedLink.txt','w')
requestObj = requests.get('https://techlekh.com/')
soup = BeautifulSoup(requestObj.text,'html.parser')

anchortags = soup.find_all('a')
for a in anchortags:
    f.write(a.text + '\n')