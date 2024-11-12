from django.contrib import admin

# Register your models here.
from apps.order.models import Order

admin.site.register(Order)