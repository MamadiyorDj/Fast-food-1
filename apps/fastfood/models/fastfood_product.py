from django.db import models
from .fastfoods import Fastfood
from apps.product.models.products import Product
# Create your models here.


class FastFoodParent(models.Model):
    fastfood = models.ForeignKey(Fastfood, on_delete=models.CASCADE, related_name='fastfood')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fastfoodparent')

    def __str__(self):
        return self.fastfood.name

    class Meta:
        ordering = ['-id']