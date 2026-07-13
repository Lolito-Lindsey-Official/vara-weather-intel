# main file of the vara app

from weather import get_weather
from decision import decision_engine

print("VĀRA Weather Intel v0.01")

city = input("What city would you like analyzed? ")

weather_data = get_weather(city)

# sample pulled data

"""
{'coord': {'lon': -87.65, 'lat': 41.85}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 'base': 'stations', 'main': {'temp': 14.72, 'feels_like': 14.7, 'temp_min': 13.64, 'temp_max': 15.57, 'pressure': 1011, 'humidity': 94, 'sea_level': 1011, 'grnd_level': 989}, 'visibility': 7696, 'wind': {'speed': 1.79, 'deg': 58, 'gust': 3.13}, 'rain': {'1h': 3.17}, 'clouds': {'all': 100}, 'dt': 1782104707, 'sys': {'type': 2, 'id': 2075214, 'country': 'US', 'sunrise': 1782123353, 'sunset': 1782178155}, 'timezone': -18000, 'id': 4887398, 'name': 'Chicago', 'cod': 200}
"""

temp = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]
wind = weather_data["wind"]["speed"]
humidity = weather_data["main"]["humidity"]
visibility = weather_data["visibility"]

visibility_m = visibility
visibility_km = visibility_m / 1000

print(f"Temperature: {temp} C")
print(f"Conditions: {description}")
print(f"Wind Speed: {wind} m/s")
print(f"Humidity: {humidity} %")
print(f"Visibility Distance: {visibility_km:.1f} km")

decision = decision_engine(description, temp, wind, humidity, visibility)
print(f"Decision: {decision}")


