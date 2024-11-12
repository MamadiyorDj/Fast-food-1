from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    Users_role = {
        (1,  ("Super admin")),
        (2,  ("Officiant")),
        (3,  ("User")),
    }
    password = models.CharField(max_length=1000)
    birth_date = models.DateTimeField(auto_now_add=True)
    user_role = models.CharField(choices=Users_role, default=3, max_length=1)
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=255)
    image = models.ImageField(width_field=5000, height_field=5000)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        app_label = 'account'
