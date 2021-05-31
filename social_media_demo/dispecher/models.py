from os import name
from django.db import models

# Create your models here.


class Person(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="images")
    bio = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name  + ' ' + self.last_name
