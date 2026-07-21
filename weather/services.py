import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("cod") == 200:
            return {
                "icon": data["weather"][0]["icon"],
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "min_temp": round(data["main"]["temp_min"]),
                "max_temp": round(data["main"]["temp_max"]),
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "visibility": round(data["visibility"] / 1000),
                "wind": data["wind"]["speed"],
                "icon": data["weather"][0]["icon"],
                "date": datetime.now().strftime("%d %B %Y"),
                "time": datetime.now().strftime("%I %M %p"),
            }

    return None