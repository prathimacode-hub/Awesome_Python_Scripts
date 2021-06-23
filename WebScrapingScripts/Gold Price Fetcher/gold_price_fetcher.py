import requests
from bs4 import BeautifulSoup

#Getting the url
page = requests.get("https://www.goodreturns.in/gold-rates/")
Soup = BeautifulSoup(page.content,'html.parser')

#finding the proper data
info = Soup.find_all(class_="odd_row")
count = 0

#proper fomatting of data
for items in info:
    count +=1
    if count ==2:
        print(items.get_text())
        break