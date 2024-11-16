from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/images")
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_on = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    pass


    