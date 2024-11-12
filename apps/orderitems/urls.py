from django.urls import path
from .views import *


urlpatterns = [
    path('orderitem', OrderItemList.as_view(), name='orderitem_list'),
    path('orderitem/<int:pk>', OrderItemDetail.as_view(), name='orderitem_detail'),
    path('orderitem/create',OrderItemCreate.as_view(), name='orderitem_create'),
    path('orderitem/delete/<int:pk>', OrderItemDelete.as_view(), name='orderitem_delete'),
]