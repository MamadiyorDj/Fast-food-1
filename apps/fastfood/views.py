from rest_framework.generics import *
from apps.fastfood.serializers.serializers import *
from rest_framework.permissions import *
from apps.product.permission.permission import *

# Create your views here.


class FastfoodList(ListAPIView):
    queryset = Fastfood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [AllowAny]


class FastfoodDetail(RetrieveAPIView):
    queryset = Fastfood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [AllowAny]


class FastfoodCreate(CreateAPIView):
    queryset = Fastfood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [MyUserPermissions]


class FastfoodDelete(DestroyAPIView):
    queryset = Fastfood.objects.all()
    serializer_class = FastFoodSerializer
    permission_classes = [MyUserPermissions]


class FastfoodParentList(ListAPIView):
    queryset = FastFoodParent.objects.all()
    serializer_class = FastFoodParentSerializer
    permission_classes = [AllowAny]


class FastfoodParentDetail(RetrieveAPIView):
    queryset = FastFoodParent.objects.all()
    serializer_class = FastFoodParentSerializer
    permission_classes = [AllowAny]


class FastfoodParentCreate(CreateAPIView):
    queryset = FastFoodParent.objects.all()
    serializer_class = FastFoodParentSerializer
    permission_classes = [MyUserPermissions]


class FastfoodParentDelete(DestroyAPIView):
    queryset = FastFoodParent.objects.all()
    serializer_class = FastFoodParentSerializer
    permission_classes = [MyUserPermissions]