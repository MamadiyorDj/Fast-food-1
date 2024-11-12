from django.db import models
from apps.order.models.orders import Order
from apps.product.models.products import Product
from geopy.distance import distance


class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, blank=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    total = models.IntegerField(default=0, blank=True)
    delivery_time = models.IntegerField(default=0, blank=True)

    @property
    def discounted_price(self):
        if self.product.discount:
            total = int(self.product.price * self.product.discount / 100) * int(self.quantity)
        else:
            total = int(self.product.price) * int(self.quantity)
        return total

    @property
    def discounted_time(self):
        if (self.quantity % 4) == 0:
            total_time = self.quantity // 4 * 5
        else:
            total_time = (self.quantity // 4 + 1) * 5
        distanc = distance((self.order.latitude, self.order.longitude),
                           (self.order.fastfood_id.latitude, self.order.fastfood_id.longitude)).kilometers

        time = distanc * 3 + total_time
        if time % 1 == 0:
            return time
        else:
            return int(time // 1 + 1)

    def __str__(self):
        return self.order.user.username

    class Meta:
        ordering = ['-id']

