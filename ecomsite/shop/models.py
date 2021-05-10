from django.db import models

# Create your models here.


class Product(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=300)
