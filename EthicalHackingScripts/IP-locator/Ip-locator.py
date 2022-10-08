#usr/bin/env python

import requests 
 

user_in = input("Enter the ip Address : ")
url_gen = 'http://ip-api.com/json/'+ user_in

print(url_gen)

ip_data = None

try:
    ip_data = requests.get(url_gen)
except:
    
    print("Please! Check your internet connection")
    
if (ip_data != None):
	r = requests.get(url_gen)
	file = r.json()                                                 
	
	country = file['country']
	countryCode = file['countryCode']
	region  = file['region' ]
	regionName = file['regionName']
	city = file['city']
	zip_ = file['zip']
	lat = file['lat']
	lon = file['lon']
	timezone = file['timezone']
	isp = file['isp']
	org = file['org']

	print('''


	................_script copyright Karan Sharma_................


	 country =  {0} \n
	 countryCode = {1} \n
	 region = {2} \n
	 regionName = {3}\n
	 city =  {4}\n
	 zip =  {5}\n
	 lat = {6}\n
	 lon =  {7}\n
	 timezone = {8}\n
	 isp = {9}\n
	'''.format(country,countryCode,region,regionName,city,zip_,lat,lon,timezone,isp)
	)
	
	print(url_gen)
