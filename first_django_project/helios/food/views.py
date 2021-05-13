from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from food.models import Food

# Create your views here.


def home_view(request, *args, **kwargs):
    users = User.objects.all()
    food = Food.objects.all()

    context = {
        'users': users,
        'food': food,
    }
    return render(request, 'home.html', context)


def catalog_view(request, *args, **kwargs):
    food = Food.objects.all()

    context = {
        'food': food,
    }
    return render(request, 'catalog.html', context)

def price_view(request,pk , *args, **kwargs):
    product = Food.objects.get(id=pk)

    context = {
        'product': product,
    }
    return render(request, 'price.html', context)



