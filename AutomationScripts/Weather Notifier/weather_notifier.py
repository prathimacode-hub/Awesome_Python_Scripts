# import Libraries
import time
import requests
import  json
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
#  Defination of function to fetch the data 
def update():
    # Take Inout From User
    city=input("enter name of the city")
    # google search done by program itself similar to web scraping
    search="weather in"+city
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    print(r)
    s= BeautifulSoup(r.text,"html.parser")
    print(s)
    update=s.find("div",class_="BNeawe").text
    print(update)
    # format to print the Notification 
    text= f'Temperature in {city} in degree celsius is  \n{update}'
    while True:
        toast=ToastNotifier()
        # time duration for getting notified 
        toast.show_toast("weather Update",text, duration=20)
        time.sleep(10)
# calling update function
update()
        
