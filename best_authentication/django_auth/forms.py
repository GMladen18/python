from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms

from django_auth.models import UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email' , 'password1' ,'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('E-mail is required!')
        return email

class ProfileRegistration(forms.ModelForm):
        class Meta:
            model = UserProfile
            exclude = ('user',)

