from django.urls import path
from .views import *


urlpatterns = [
    path('category', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('category/create', CategoryCreate.as_view(), name='category_create'),
    path('category/delete/<int:pk>', CategoryDelete.as_view(), name='category_delete'),
    path('product/', ProductList.as_view(), name='product'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/create', ProductCreate.as_view(), name='product_create'),
    path('product/delete/<int:pk>', ProductDelete.as_view(), name='product_delete'),
]
