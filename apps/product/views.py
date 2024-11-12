from apps.product.permission.permission import MyUserPermissions
from apps.product.serializers.serializers import *
from rest_framework.generics import *
from apps.product.models.products import *
from rest_framework.permissions import *
# Create your views here.


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [MyUserPermissions]


class CategoryDelete(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [MyUserPermissions]


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [MyUserPermissions]


class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [MyUserPermissions]