# Import following modules
from geopy.geocoders import Nominatim  # pip install geopy
from geopy.distance import geodesic
# Link the user_agent to Google Map, so tat it can calculate latitude and longitude
geolocator = Nominatim(user_agent="https://maps.google.com")
fro = input("From: ")  # From which City
to = input("To: ")  # To which city
try:
    location = geolocator.geocode(fro)  # Fetch all the data of the city
    locate = geolocator.geocode(to)
    # Extract longitude and latitude
    newport_ri = (location.latitude, location.longitude)
    cleveland_oh = (locate.latitude, locate.longitude)
    # Display the distance in KiloMeters
    dist = format(geodesic(newport_ri, cleveland_oh).km, '.1f')
    dist = "{:,}".format(float(str(dist)))
    print(f"Distance: {dist} km")
except:
    print("No result found!")
