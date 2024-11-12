from django.contrib import admin

# Register your models here.
from apps.fastfood.models import *

admin.site.register(Fastfood)
admin.site.register(FastFoodParent)