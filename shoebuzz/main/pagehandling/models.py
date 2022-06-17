from distutils.command.upload import upload
from django.db import models
# Create your models here.

#this code adds a group in django admin page (add class in admin.py)
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField()
