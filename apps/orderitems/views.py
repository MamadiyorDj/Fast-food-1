from rest_framework.generics import *
from .serializers.serializers import OrderItemSerializer
from apps.order.permissions.permissions import MyUserPermissions
from apps.orderitems.models.orderitems import Orderitem

# Create your views here.


class OrderItemList(ListAPIView):
    queryset = Orderitem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [MyUserPermissions]


class OrderItemDetail(RetrieveAPIView):
    queryset = Orderitem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [MyUserPermissions]


class OrderItemCreate(CreateAPIView):
    queryset = Orderitem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [MyUserPermissions]


class OrderItemDelete(DestroyAPIView):
    queryset = Orderitem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [MyUserPermissions]