from django.contrib import admin

# Register your models here.
from apps.orderitems.models import Orderitem

admin.site.register(Orderitem)