# import the phonenumbers module to use it in this program
import phonenumbers

# From phonenumbers module we've to import 2 more libraries geocoder and carrier
from phonenumbers import geocoder
from phonenumbers import carrier

# Take the user input
PhoneNumber = input("Enter Phone Number: ")
number = phonenumbers.parse(PhoneNumber)

# Fetch the details from modules and store it in variables
country = ("Country: " + geocoder.description_for_number(number, "en"))
sp = ("Service Provider: " + carrier.name_for_number(number, "en"))

# Print the output
print(country)
print(sp)
