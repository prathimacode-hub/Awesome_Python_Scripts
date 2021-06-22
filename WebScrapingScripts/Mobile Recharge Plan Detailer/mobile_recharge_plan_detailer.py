import requests
from bs4 import BeautifulSoup

#getting detail of users service provider
user= (input("enter your service provider : "))
url ="https://www.91mobiles.com/recharge-plans/"+user+"-prepaid-gujarat-unlimited"

#fetching information from website
page =requests.get(url)
Soup =BeautifulSoup(page.content,'html.parser')

#proper formatting of output
info =Soup.find_all(class_='ofr-desc')
a= [items.get_text() for items in info]

for i in a:
  print(i)
