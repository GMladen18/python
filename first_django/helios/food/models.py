from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField()
    is_promo = models.BooleanField(default=False)
