# https://stackoverflow.com/questions/75637770/django-relation-of-model
from django.db import models
from apps.account.models.users import User
from apps.fastfood.models.fastfoods import Fastfood
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fastfood = models.ForeignKey(Fastfood, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=255, blank=True)
    delivery_phone = PhoneNumberField(blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['id']

