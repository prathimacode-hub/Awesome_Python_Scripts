import requests

# API link:- https://disease.sh/v3/covid-19/all

response = requests.get('https://disease.sh/v3/covid-19/all')
# print(response.status_code) #To check whether API call is successful or not
# print(response.text) # To access all the content of the website
print(response.url) # url of the website to which we made our API call
