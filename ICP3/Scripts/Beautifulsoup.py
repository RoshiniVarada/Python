import requests
from bs4 import BeautifulSoup

Link=requests.get("https://en.wikipedia.org/wiki/Deep_learning")
Bsoup=BeautifulSoup(Link.text,"html.parser")

print(Bsoup.find('title').string)

outfile=open('output.txt','a+',encoding='utf-8')

for atag in  Bsoup.find_all('a'):
    if atag.get('href'):
        outfile.write(str(atag.get('href'))+'\n')
        print(atag.get('href'))

