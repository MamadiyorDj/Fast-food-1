from rest_framework.serializers import ModelSerializer
from apps.orderitems.models.orderitems import Orderitem


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = Orderitem
        fields = '__all__'