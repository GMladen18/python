from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='profiles/')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
