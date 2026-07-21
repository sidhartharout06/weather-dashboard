from django.shortcuts import render
from .services import get_weather, get_weather_by_coordinates


def home(request):
    city = request.GET.get("city", "").strip()

    weather = None

    if city:
        weather = get_weather(city)

    context = {
        "city": city,
        "weather": weather,
    }

    return render(request, "weather/home.html", context)


def location_weather(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    weather = None

    if lat and lon:
        weather = get_weather_by_coordinates(lat, lon)

    context = {
        "city": weather["city"] if weather else "",
        "weather": weather,
    }

    return render(request, "weather/home.html", context)
