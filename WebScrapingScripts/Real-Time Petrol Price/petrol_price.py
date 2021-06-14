# requests module allows you to send HTTP requests and returns a Response Object with all the response​.
import requests
# Pandas dataframe is 2D size-mutable,tabular data with labeled axes
import pandas as pd
# BeautifulSoup is a python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
def getdata(url):
    r=requests.get(url) # Accessing all required data from url site and store in data.
    return r.text
htmldata=getdata("https://www.goodreturns.in/petrol-price.html") 
soup=BeautifulSoup(htmldata,'html.parser') # It takes text of page as argument and then parse it with html.parser
mydatastr='' #initialize the table str with null
result=[]
for table in soup.find_all('tr'):
    mydatastr+=table.get_text()
mydatastr=mydatastr[1:]
itemlist=mydatastr.split("\n\n")
for item in itemlist[:-5]:
    result.append(item.split("\n"))
df=pd.DataFrame(result[:-8]) # DataFrame align the data in a tabular fashion in rows and columns
print(df)
