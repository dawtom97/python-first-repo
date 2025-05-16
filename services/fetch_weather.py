import requests
from utils.to_celsius import to_celsius
from utils.ms_to_kmh import ms_to_kmh
import time

def fetch_weather(token: str,city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"
    response = requests.get(url)
    data = response.json()

    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")

    weather = {
            "timestamp": timestamp,
            "name": data["name"],
            "temp": to_celsius(data["main"]["temp"]),
            "feels_like": to_celsius(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": ms_to_kmh(data["wind"]["speed"])
    }
    return weather


