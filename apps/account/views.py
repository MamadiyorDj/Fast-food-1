from apps.product.permission.permission import MyUserPermissions
from apps.account.models.users import User
from apps.account.serializers.serializers import UserSerializer
from rest_framework.generics import *


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [MyUserPermissions]


class UserRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [MyUserPermissions]

