# fetching weather details of any particular city using OpenWeatherMap API

import requests
import time

try:
    city = input("Enter the city name--")
    # create and use your own appid
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=<put-your-appid-here>"
    w_data = requests.get(api).json()

    weather = w_data['weather'][0]['main']
    temp = int(w_data['main']['temp'] - 273.15)
    temp_min = int(w_data['main']['temp_min'] - 273.15)
    temp_max = int(w_data['main']['temp_max'] - 273.15)

    pressure = w_data['main']['pressure']
    humidity = w_data['main']['humidity']
    visibility = w_data['visibility']

    wind = w_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

    all_data1 = f"Weather condition: {weather} \nTemperature: {str(temp)}°C\n"
    all_data2 = f"Minimum Temperature: {str(temp_min)}°C \n" \
                f"Maximum Temperature: {str(temp_max)}°C \n" \
                f"Pressure: {str(pressure)} millibar \n" \
                f"Humidity: {str(humidity)}% \n\n" \
                f"Visibility: {str(visibility)} metres \n" \
                f"Wind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                f"\nSunset: {sunset}"
    print(f"Weather information for {city.capitalize()}...")
    print(all_data1)
    print(all_data2)

except Exception as e:
    pass

