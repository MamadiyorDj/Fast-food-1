from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField()
    price = models.IntegerField()
    description = models.TextField()
    active = models.BooleanField(default=True)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
