from django.urls import path
from .views import *


urlpatterns = [
    path('fastfood', FastfoodList.as_view(), name='fastfood_list'),
    path('fastfood/<int:pk>', FastfoodDetail.as_view(), name='fastfood_detail'),
    path('fastfood/create', FastfoodCreate.as_view(), name='fastfood_create'),
    path('fastfood/delete/<int:pk>', FastfoodDelete.as_view(), name='category_delete'),
    path('fastfood_parent', FastfoodParentList.as_view(), name='fastfood_parent'),
    path('fastfood_parent/<int:pk>', FastfoodParentDetail.as_view(), name='fastfood_parent_detail'),
    path('fastfood_parent/create', FastfoodParentCreate.as_view(), name='fastfood_parent_create'),
    path('fastfood_parent/delete/<int:pk>', FastfoodParentDelete.as_view(), name='fastfood_parent_delete'),
]