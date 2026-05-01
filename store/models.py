from django.db import models
from django.contrib.auth.models import User


# 👤 CUSTOMER PROFILE
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


# 🛒 PRODUCT
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name