# importing the psutil library
import psutil

data = psutil.sensors_temperatures()
print("Current Temperature of CPU (celcius): ", data['coretemp'][0][1])