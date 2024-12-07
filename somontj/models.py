from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class ProductManager(models.Manager):
    def active(self):
        return self.filter(deleted=False)
    
    def deleted(self):
        return self.filter(deleted=True)
    
    def soft_delete(self, product_id):
        product = self.get(id=product_id)
        product.deleted = True
        product.deleted_at = timezone.now()
        product.save()
    
    def restore(self, product_id):
        product = self.get(id=product_id)
        product.deleted = False
        product.deleted_at = None
        product.save()
    
    def hard_delete(self, product_id):
        product = self.get(id=product_id)
        product.delete()

    def total_products(self):
        return self.filter(deleted=False).count()


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/images")
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_on = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    objects = ProductManager()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    pass






    