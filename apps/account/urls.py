from .views import *
from django.urls import path


urlpatterns = [
    path('users', UserList.as_view(), name='users'),
    path('users/<int:pk>', UserRetrieve.as_view(), name='users_retrieve'),
]