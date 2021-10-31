import json
import requests
import smtplib

input_city = str(input("enter city name : "))
sender_email = str(input("enter sender's email ID : "))
sender_pwd = str(input("enter sender's email password : "))
receiver_email = str(input("enter receiver's email ID : "))
API_key = str(input("enter the API key : "))

input_city = input_city.lower()
input_city_list = list(input_city)
input_city_list[0] = input_city_list[0].upper()
for i in range(1, len(input_city_list)):
	if(input_city_list[i-1]==' '):
		input_city_list[i] = input_city_list[i].upper()

input_city = ''.join(input_city_list)

json1_file = open('city_list.json', encoding="utf8")
json1_str = json1_file.read()
json1_data = json.loads(json1_str)

coord_city_list = []
count_cities = 0
message = ""
for i in range(len(json1_data)):
	if(json1_data[i]['name']==input_city):
		count_cities = count_cities + 1
		coord_dict = json1_data[i]['coord']
		coord_list = []
		coord_list.append(coord_dict['lon'])
		coord_list.append(coord_dict['lat'])
		coord_city_list.append(coord_list)
		lat = coord_list[1]
		lon = coord_list[0]
		url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(lat) + "&lon=" + str(lon) + "&exclude=current,minutely,daily,alerts&appid=" + API_key
		req = requests.get(url)
		req_text = req.text
		c = 0
		start_idx = 0
		while(c!=12):
			find_idx = req_text.find("main", start_idx)
			start_idx = find_idx+1
			c = c+1
		find_idx = req_text.find("main", start_idx)
		find_idx = find_idx+7
		weather_condition = ""
		while(req_text[find_idx]!=","):
			weather_condition = weather_condition + req_text[find_idx]
			find_idx = find_idx + 1
		weather_condition = weather_condition[0:len(weather_condition)-1]
		message = message + "the 12 hour weather forecast of city " + input_city + " with country initials " + json1_data[i]['country'] + " is : " + weather_condition.upper() + "." + "\n"

if(count_cities==0):
	message = "unfortunately we did not find your entered city name in our database. Please check for any spelling errors."

elif(count_cities==1):
	message = "we found " + str(count_cities) + " city with name " + input_city + "." + "\n" + message
		
elif(count_cities>1):
	message = "we found " + str(count_cities) + " cities with name " + input_city + "." + "\n" + message

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, sender_pwd)
server.sendmail(sender_email, receiver_email, message)
server.quit()

