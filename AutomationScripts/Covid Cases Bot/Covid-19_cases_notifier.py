import platform, notify2
import time
import requests
import  json
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

def covidbot(count=2,timeout=10):
    while count != 0:
        r=requests.get(url)
        data=r.json()
        text= f'confirmed cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
        try:
            func[os](text)
        except KeyError:
            print('not supported OS')
            exit()
        time.sleep(timeout)
        count -= 1

def covidbot_Linux(text):
    notify2.init('covidbot')
    message = notify2.Notification(text)
    message.show()

def covidbot_Windows(text):   
    from win10toast import ToastNotifier
    toast=ToastNotifier()
    toast.show_toast("covid - 19 updates",text, duration=20)

url = 'https://coronavirus-19-api.herokuapp.com/all'
os = platform.system()
func = {'Windows':covidbot_Windows, 'Linux':covidbot_Linux}

if __name__ == '__main__':
    covidbot()
