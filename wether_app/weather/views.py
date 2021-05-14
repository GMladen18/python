from django import forms
from django.conf.urls import url
from django.shortcuts import render
import requests

from weather.models import City
from weather.forms import CityForm


# Create your views here.

def index_view(request, *args, **kwargs):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=6bd02d1ff7c484bb30c023666e9004e4'

    if request.method == 'POST':
        print(request)
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        response = requests.get(url.format(city.name))
        if response.ok:
            city_weather = response.json()
        else:
            break
           
        temp = city_weather['main']['temp'] - 272.15

        
        weather = {
            'city': city,
            'temperature': temp,
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form }
    return render(request, 'index.html', context)



