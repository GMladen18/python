from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def home_view(request, *args , **kwargs):
    user = request.user
    context = {
            'user' : user,
    }

    return render(request, 'home.html' , context)