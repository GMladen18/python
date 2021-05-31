from genericpath import isfile
from os.path import join
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.urls.conf import path


from dispecher.forms import SignUpForm, LoginForm, PersonForm

# Create your views here.


def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home/home.html', context)


def sign_up_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home_view)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home_view)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_edit_view(request, *args, **kwargs):
    if request.method == 'GET':
        context = {
            'form': PersonForm()
            }
        return render(request, 'edit-profile.html', context)
    else:
        form = PersonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(home_view)

        context = {
            'form': form
            }  
    return render(request, 'edit-profile.html',context )




    


 
