import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timezone, timedelta

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")



def get_wind_direction(degree):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(degree / 45) % 8
    return directions[index]


def format_weather_data(data):
    city_timezone = timezone(timedelta(seconds=data["timezone"]))
    city_time = datetime.now(city_timezone)

    weather = data["weather"][0]["main"]
    icon = data["weather"][0]["icon"]

    if weather == "Clear":
        background = "night_sky.jpeg" if icon.endswith("n") else "sunny.jpeg"

    elif weather == "Clouds":
        background = "cloudy.jpeg"

    elif weather in ["Rain", "Drizzle"]:
        background = "rainy.jpeg"

    elif weather == "Thunderstorm":
        background = "thunderstorm.jpeg"

    elif weather == "Snow":
        background = "snow.jpeg"

    elif weather in ["Mist", "Fog", "Haze", "Smoke", "Dust"]:
        background = "fog.jpeg"

    else:
        background = "sunny.jpeg"

    return {
        "icon": icon,
        "background": background,
        "main_weather": weather,
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
        "wind_direction": get_wind_direction(
            data["wind"].get("deg", 0)
        ),
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
    
def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("cod") == 200:
            return format_weather_data(data)

    return None



def get_weather_by_coordinates(lat, lon):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("cod") == 200:
            return format_weather_data(data)

    return None