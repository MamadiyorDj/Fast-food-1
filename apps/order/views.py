from apps.order.models.orders import Order
from rest_framework.generics import *
from apps.order.permissions.permissions import MyUserPermissions
from apps.order.serializers.serializers import OrderSerializer
# Create your views here.


class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [MyUserPermissions]


class OrderDetail(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [MyUserPermissions]


class OrderCreate(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [MyUserPermissions]


class OrderDelete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [MyUserPermissions]
