from rest_framework.serializers import *
from apps.order.models.orders import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'