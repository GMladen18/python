from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django_auth.forms import RegistrationForm, ProfileRegistration

# Create your views here.


@transaction.atomic
def registration_view(request, *args, **kwargs):
    if request.method == "GET":
        context = {
            'user_form': RegistrationForm(),
            'profile_form': ProfileRegistration(),
        }
        return render(request, 'registration/signup.html', context)

    else:
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileRegistration(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            redirect('home')

        context = {
            'user_form': RegistrationForm(),
            'profile_form': ProfileRegistration(),
        }

    return render(request, 'registration/signup.html', context)


def logout_view(request, *args, **kwargs):
    logout(request)
    context = {}
    return render(request, 'home.html', context)
