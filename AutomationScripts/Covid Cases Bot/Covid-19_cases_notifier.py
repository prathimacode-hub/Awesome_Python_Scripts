import platform, notify2
import time
import requests
import  json
from bs4 import BeautifulSoup
#import math ## for continuous iteration

# cheking the avialability of the module
try:
    from win10toast import ToastNotifier
except ModuleNotFoundError:
    if platform.system() == 'Windows':
        print('module "win10toast" not found')
        exit()

def covidbot(count=2,timeout=10): # for continuous iteration covidbot(count=math.inf)
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

# called in linux
def covidbot_Linux(text):
    notify2.init('covidbot')
    message = notify2.Notification(text)
    message.show()

# called in windows
def covidbot_Windows(text):   
    toast=ToastNotifier()
    toast.show_toast("covid - 19 updates",text, duration=20)

os = platform.system() #determining the OS type
url = 'https://coronavirus-19-api.herokuapp.com/all'
func = {'Windows':covidbot_Windows, 'Linux':covidbot_Linux} 

if __name__ == '__main__':
    covidbot()
