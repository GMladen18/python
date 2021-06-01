from authentication.forms import LoginForm, ProfileForm, RegistrationForm
from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib.auth import authenticate,login , logout


# Create your views here.


def home_view(request, *args, ** kwargs):
    context = {}
    return render(request, 'home.html', context)




def login_view(request, *args, ** kwargs):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(request , 'auth/login.html', context)
    else:

        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username , password = password)

        if user:
            login(request , user)
            return redirect('home view')
    context = {
            'login_form': login_form,
        }
    return render(request , 'auth/login.html', context)

@transaction.atomic
def register_view(request , *args, ** kwargs):
    if request.method == "GET":
        context = {
            'user_form' : RegistrationForm(),
            'profile_form' : ProfileForm(),
        }

        return render(request , 'auth/register.html' , context)

    elif request.method == 'POST':

        user_form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST , request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request , user)
            return redirect('home view')

    context = {
            'user_form' : RegistrationForm(),
            'profile_form' : ProfileForm(),
        }
    return render(request , 'auth/register.html' , context)



def logout_view(request , *args, ** kwargs):
    logout(request)
    return redirect('home view')

