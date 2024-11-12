from django.db import models


class Fastfood(models.Model):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
