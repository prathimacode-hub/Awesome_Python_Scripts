# import the phonenumbers module to use it in this program
import phonenumbers
# geocoder: to know the specific location to that phone number 
# carrier: to know the name of service provider of that phone
from phonenumbers import geocoder
from phonenumbers import carrier
phone_number = phonenumbers.parse("Number with country code")
service_provider = phonenumbers.parse("Number with country code") 
# this will print the country name 
print(geocoder.description_for_number(phone_number,'en'))
#this will print the service provider name 
print(carrier.name_for_number(service_provider,'en'))  

                                      
