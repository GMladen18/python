from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        query_set = User.objects.filter(username__iexact=username)

        if query_set.exists():
            raise forms.ValidationError("This username is invalid. Please pick another!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        query_set = User.objects.filter(email__iexact=email)

        if query_set.exists():
            raise forms.ValidationError("This email is invalid. Please pick another!")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        query_set = User.objects.filter(username__iexact=username)

        if not query_set.exists():
            raise forms.ValidationError("This is invalid username")
        return username
