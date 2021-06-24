# json convert the python dictionary above into a json
import json  
import turtle
# urllib.request fetch URLs using a variety of different protocols
import urllib.request 
import time 
# webbrowser provides a high-level interface to allow displaying Web-based documents to users
import webbrowser 
# geocoder takes the data and locate these locations in the map
import geocoder

url = "http://api.open-notify.org/astros.json" 
response = urllib.request.urlopen(url) 
result = json.loads(response.read())
file = open("iss.txt", "w") 
file.write("There are currently " +
           str(result["number"]) + " astronauts on the ISS: \n\n") # prints number of astronauts
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n") # prints names of crew 
# print long and lat
g = geocoder.ip('me') 
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image
screen.bgpic("images/map.gif")
screen.register_shape("images\iss.gif")
iss = turtle.Turtle()
iss.shape("images\iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Ouput lon and lat to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 seconds
    time.sleep(5)

