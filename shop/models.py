from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"ID: {self.id} | {self.title} |"


class Order(models.Model):
    items = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    ordered = models.BooleanField(default=False)
    def __str__(self):
    return f"ID: {self.id} | {self.name} |"
