import requests
from bs4 import BeautifulSoup

x=requests.get("https://www.bbc.com/news")

page=x.text


soup=BeautifulSoup(page,"html.parser")

links=soup.findAll("img")

for i in links:
    print(i.get("href"))
    




