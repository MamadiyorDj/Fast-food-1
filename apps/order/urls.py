from django.urls import path
from .views import *


urlpatterns = [
    path('order', OrderList.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order_detail'),
    path('order/create',OrderCreate.as_view(), name='order_create'),
    path('order/delete/<int:pk>', OrderDelete.as_view(), name='order_delete'),
]