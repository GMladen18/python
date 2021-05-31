from dispecher.models import Person
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.db.models import fields

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',  'password1')
        # fields = '__all__'

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = ('username',  'password1')
        fields = '__all__'
