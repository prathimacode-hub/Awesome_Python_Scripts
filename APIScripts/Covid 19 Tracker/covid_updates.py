import requests
import json

# API link:- https://disease.sh/v3/covid-19/all

response = requests.get('https://disease.sh/v3/covid-19/all')
# print(response.status_code) #To check whether API call is successful(200) or not(404)
# print(response.text) # To access all the content of the website
# print(response.url) # url of the website to which we made our API call

python_data = json.loads(response.text)
print(type(python_data))
for key in python_data.keys():
    print(f'{key} : {python_data[key]}')