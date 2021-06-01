
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='teams')
    players = models.ManyToManyField(User, related_name='teams')
    created_by = models.OneToOneField(User , related_name='creaated_teams', on_delete=models.CASCADE , null=True)
    

    def __str__(self):
        return self.name


