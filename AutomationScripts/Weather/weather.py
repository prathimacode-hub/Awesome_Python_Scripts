import time
import requests
import  json
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
def update():
    city=input("enter name of the city")
    search="weather in"+city
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    print(r)
    s= BeautifulSoup(r.text,"html.parser")
    print(s)
    update=s.find("div",class_="BNeawe").text
    print(update)
    text= f'Temperature in {city} in degree celsius is  \n{update}'
    while True:
        toast=ToastNotifier()
        toast.show_toast("weather Update",text, duration=20)
        time.sleep(10)
update()
        
        
