from django.db import models
# Create your models here.

#this code adds a group in django admin page (add class in admin.py)
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField()

class user(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return "%s%s"%(self.firstname,self.lastname)