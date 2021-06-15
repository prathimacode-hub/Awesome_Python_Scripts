import time
import requests
import  json
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
def covidbot():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    print(data)
    text= f'confirmed cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
    while True:
        toast=ToastNotifier()
        toast.show_toast("covid - 19 updates",text, duration=20)
        print("Covid - 19 updates",text)
        time.sleep(10)
covidbot()
