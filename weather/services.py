import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta

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
        city_timezone = timezone(timedelta(seconds=data["timezone"]))
        city_time = datetime.now(city_timezone)

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
                "date": city_time.strftime("%d %B %Y"),
                "time": city_time.strftime("%I:%M %p"),

                "sunrise": datetime.fromtimestamp(
                    data["sys"]["sunrise"],
                    tz=city_timezone
                ).strftime("%I:%M %p"),

                "sunset": datetime.fromtimestamp(
                    data["sys"]["sunset"],
                    tz=city_timezone
                ).strftime("%I:%M %p"),
            }

    return None