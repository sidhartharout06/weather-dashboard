from django.shortcuts import render
from .services import (
    get_weather,
    get_weather_by_coordinates,
    get_forecast,
    get_forecast_by_coordinates,
)


def home(request):
    city = request.GET.get("city", "").strip()

    weather = None
    forecast = None

    if city:
        weather = get_weather(city)
        forecast = get_forecast(city)
        print(forecast)

    context = {
        "city": city,
        "weather": weather,
        "forecast": forecast,
    }

    return render(request, "weather/home.html", context)


def location_weather(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    weather = None
    forecast = None

    if lat and lon:
        weather = get_weather_by_coordinates(lat, lon)
        forecast = get_forecast_by_coordinates(lat, lon)


    context = {
        "city": weather["city"] if weather else "",
        "weather": weather,
        "forecast": forecast,
    }

    return render(request, "weather/home.html", context)
