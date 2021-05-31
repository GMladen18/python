from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    profile_image = models.ImageField(upload_to='' )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
