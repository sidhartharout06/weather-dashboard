from django.shortcuts import render
from .services import get_weather


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