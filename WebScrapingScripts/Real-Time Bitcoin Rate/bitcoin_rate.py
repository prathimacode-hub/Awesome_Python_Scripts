# BeautifulSoup is a python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup as BS
# requests module allows you to send HTTP requests and returns a Response Object with all the response​.
import requests
def get_price(url):
    data=requests.get(url) # Accessing all required data from url site and store in data.
    soup=BS(data.text,"html.parser") # It takes text of page as argument and then parse it with html.parser
    ans=soup.find("div",class_="BNeawe iBp4i AP7Wnd").text # here the class name is passed as argument to find out that particular info in html text
    return ans
url="https://www.google.com/search?q=bitcoin+price"
ans=get_price(url)
print("1 Bitcoin = ",ans)
