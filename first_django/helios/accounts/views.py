from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User

from accounts.forms import LoginForm ,RegisterForm

# Create your views here.
def register_view(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        try:
            user = User.objects.create_user(username,email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/home")


    return render(request, "login.html", {"form": form})

def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        cleaned_data = form.cleaned_data

        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect("/home")
        else:
            request.session['attemt'] += 1
            #  return redirect("/invalid-password")

    return render(request, "login.html", {"form": form})

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("/login")

