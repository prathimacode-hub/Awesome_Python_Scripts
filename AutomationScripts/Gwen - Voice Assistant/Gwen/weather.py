import requests

from api import *

api_address='http://api.openweathermap.org/data/2.5/weather?q=Dehradun&appid=' + api
data=requests.get(api_address).json()

def des():
    description=data['weather'][0]['description']
    return description

