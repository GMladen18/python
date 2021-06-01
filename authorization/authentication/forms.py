from authentication.models import UserProfile
from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'email')
        widgets = {
            'password' : forms.PasswordInput,
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('E-mail is requered')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        )