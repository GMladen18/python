from django.forms import fields
from teams.models import Team
from django import forms


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ('created_by',)